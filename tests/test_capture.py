import unittest
from unittest.mock import patch, MagicMock
from core.capture import process_packet

class TestCapture(unittest.TestCase):

    @patch('core.capture.emit_alert')
    @patch('core.capture.save_alert')
    @patch('core.capture.detect_anomaly')
    @patch('core.capture.parse_packet')
    def test_process_packet(self, mock_parse_packet, mock_detect_anomaly, mock_save_alert, mock_emit_alert):
        mock_packet = MagicMock()
        fake_alert_data = {
            "timestamp": "2025-06-12 12:00:00",
            "src_ip": "192.168.1.100",
            "dst_ip": "192.168.1.1",
            "protocol": "TCP",
            "length": 150,
            "info": "Mock packet"
        }

        mock_parse_packet.return_value = fake_alert_data
        mock_detect_anomaly.return_value = fake_alert_data

        result = process_packet(mock_packet)

        self.assertIsNotNone(result)
        self.assertEqual(result, fake_alert_data)
        mock_parse_packet.assert_called_once_with(mock_packet)
        mock_detect_anomaly.assert_called_once_with(fake_alert_data)
        mock_save_alert.assert_called_once_with(fake_alert_data)
        mock_emit_alert.assert_called_once_with(fake_alert_data)

if __name__ == '__main__':
    unittest.main()
