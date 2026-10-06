import os
from datetime import datetime
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "vision_platform")
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database
        )
        return self.connection

    def ensure_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()

    def insert_detection(self, detection):
        self.ensure_connection()
        query = """INSERT INTO detection_logs
        (timestamp, object_class, confidence, bbox_x, bbox_y, bbox_w, bbox_h)
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            datetime.now(), detection["object_class"], detection["confidence"],
            detection["bbox_x"], detection["bbox_y"],
            detection["bbox_w"], detection["bbox_h"]
        )
        cur = self.connection.cursor()
        try:
            cur.execute(query, values)
            self.connection.commit()
        finally:
            cur.close()

    def fetch_recent_logs(self, limit=20):
        self.ensure_connection()
        cur = self.connection.cursor(dictionary=True)
        try:
            cur.execute("""SELECT log_id,timestamp,object_class,confidence,
                bbox_x,bbox_y,bbox_w,bbox_h FROM detection_logs
                ORDER BY log_id DESC LIMIT %s""", (int(limit),))
            return cur.fetchall()
        finally:
            cur.close()

    def count_logs(self):
        self.ensure_connection()
        cur = self.connection.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM detection_logs")
            return cur.fetchone()[0]
        finally:
            cur.close()
