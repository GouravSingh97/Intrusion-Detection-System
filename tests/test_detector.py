import unittest
from core.detector import detect_anomaly
import logging

logging.basicConfig(filename='logs/detector.log', level=logging.DEBUG)

class TestDetector(unittest.TestCase):
    def test_detect_anomaly(self):
        alert_data = {
            "protocol": 6,
            "source_port": 80,
            "payload": "GET / HTTP/1.1",
            "identifier": "test_anomaly"
        }
        result = detect_anomaly(alert_data)
        logging.info(f"Anomaly detection result: {result}")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
