import unittest
from core.capture import process_packet
from scapy.all import IP, TCP
class TestCapture(unittest.TestCase):
    def test_process_packet(self):
        pkt = IP(src="192.168.1.1", dst="8.8.8.8")/TCP(sport=12345, dport=80)
        result = process_packet(pkt)
        self.assertIsNotNone(result)
if __name__ == "__main__":
    unittest.main()
