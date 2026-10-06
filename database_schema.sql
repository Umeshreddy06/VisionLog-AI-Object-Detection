CREATE DATABASE IF NOT EXISTS vision_platform;
USE vision_platform;

CREATE TABLE IF NOT EXISTS detection_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    object_class VARCHAR(100) NOT NULL,
    confidence DECIMAL(5,4) NOT NULL,
    bbox_x INT NOT NULL,
    bbox_y INT NOT NULL,
    bbox_w INT NOT NULL,
    bbox_h INT NOT NULL
);

CREATE INDEX idx_detection_timestamp ON detection_logs(timestamp);
CREATE INDEX idx_detection_class ON detection_logs(object_class);

-- Check that the table was created:
SELECT * FROM detection_logs ORDER BY log_id DESC LIMIT 20;
