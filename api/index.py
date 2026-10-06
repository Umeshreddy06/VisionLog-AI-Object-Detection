from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>VisionLog AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 60px 20px;
                    background: #f5f7fa;
                }
                .card {
                    max-width: 650px;
                    margin: auto;
                    background: white;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 4px 20px rgba(0,0,0,.1);
                }
                a {
                    display: inline-block;
                    padding: 14px 25px;
                    background: #ff4b4b;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>VisionLog AI</h1>
                <h2>Real-Time Object Detection & Logging Platform</h2>
                <p>YOLOv8 Object Detection</p>
                <p>Confidence Filtering</p>
                <p>Detection Event Logging</p>
                <a href="https://visionlog-ai-object-detection-pwsxhyoksxtwrdpkd4ferp.streamlit.app/" target="_blank">
                    Launch VisionLog AI
                </a>
            </div>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))
