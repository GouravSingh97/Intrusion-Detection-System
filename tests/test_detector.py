import unittest
from core.detector import detect_anomaly
class TestDetector(unittest.TestCase):
    def test_detect_anomaly(self):
        alert_data = {"protocol": 6, "source_port": 80, "payload": "GET / HTTP/1.1"}
        result = detect_anomaly(alert_data)
        self.assertIsNotNone(result)
if __name__ == "__main__":
    unittest.main()
