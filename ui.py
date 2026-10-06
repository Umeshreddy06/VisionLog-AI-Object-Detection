import cv2
import numpy as np
import pandas as pd
import streamlit as st

from detector import ObjectDetector, DetectionLogger
from database import Database

st.set_page_config(
    page_title="VisionLog AI | Object Detection",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def get_detector():
    return ObjectDetector()

@st.cache_resource
def get_database():
    return Database()

def run_app():
    st.title("🤖 VisionLog AI")
    st.subheader("Real-Time Object Detection & Event Logging Platform")
    st.caption("Assignment 5 • YOLO • OpenCV • Streamlit • MySQL")

    detector = get_detector()
    db = get_database()

    with st.sidebar:
        st.header("Detection Controls")
        confidence = st.slider("Confidence threshold", 0.10, 0.95, 0.70, 0.05)
        classes = list(detector.class_names.values())
        default = ["person"] if "person" in classes else classes[:1]
        selected = st.multiselect(
            "Objects to detect",
            classes,
            default=default,
            help="Select one or more YOLO classes. Leave empty for all classes."
        )
        source = st.radio(
            "Input source",
            ["📷 Browser Camera", "📁 Upload Image"],
            index=0
        )
        save_events = st.checkbox("Save detections to MySQL", value=True)

    detector.set_config(confidence=confidence, selected_classes=selected)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Model", "YOLOv8n")
    c2.metric("Confidence", f"{confidence:.0%}")
    c3.metric("Selected Classes", len(selected) if selected else "All")
    try:
        total = db.count_logs()
        c4.metric("Logged Events", total)
        db_ok = True
    except Exception:
        c4.metric("Logged Events", "—")
        db_ok = False

    st.divider()

    image = None
    if source == "📷 Browser Camera":
        image = st.camera_input("Capture a frame for YOLO detection")
    else:
        image = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png", "webp"]
        )

    if image is not None:
        if hasattr(image, "getvalue"):
            data = image.getvalue()
        else:
            data = image
        frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)

        if frame is None:
            st.error("Unable to read the selected image.")
            return

        annotated, detections = detector.detect(frame)
        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        left, right = st.columns([2, 1])
        with left:
            st.image(
                annotated_rgb,
                caption="YOLO annotated output",
                use_container_width=True
            )
        with right:
            st.markdown("### Detection Results")
            if detections:
                result_df = pd.DataFrame(detections)
                result_df["confidence"] = (
                    result_df["confidence"] * 100
                ).round(1).astype(str) + "%"
                st.dataframe(result_df, use_container_width=True, hide_index=True)

                if save_events:
                    if not db_ok:
                        st.warning("MySQL is not connected. Detection is shown but cannot be logged.")
                    else:
                        logger = DetectionLogger(cooldown_seconds=0)
                        saved = 0
                        for detection in detections:
                            if logger.should_log(detection):
                                try:
                                    db.insert_detection(detection)
                                    saved += 1
                                except Exception as exc:
                                    st.error(f"MySQL logging error: {exc}")
                        st.success(f"{saved} detection event(s) saved to MySQL.")
            else:
                st.info("No selected objects detected above the confidence threshold.")

    st.divider()
    st.markdown("### 🗄️ Recent MySQL Event Logs")
    try:
        logs = db.fetch_recent_logs(20)
        if logs:
            df = pd.DataFrame(logs)
            df["confidence"] = (
                df["confidence"] * 100
            ).round(1).astype(str) + "%"
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No database events yet.")
    except Exception as exc:
        st.warning(
            "MySQL is not connected. For deployment, configure the database "
            f"secrets/environment variables. Details: {str(exc)[:180]}"
        )

    with st.expander("ℹ️ About this project"):
        st.write(
            "VisionLog AI detects objects with Ultralytics YOLO, draws bounding "
            "boxes with OpenCV, filters detections by class and confidence, and "
            "logs qualifying events to MySQL. The browser-camera mode is designed "
            "for Streamlit deployment."
        )
