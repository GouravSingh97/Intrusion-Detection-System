import unittest
from core.parser import parse_packet
from scapy.all import IP, TCP
import logging

logging.basicConfig(filename='logs/parser.log', level=logging.DEBUG)

class TestParser(unittest.TestCase):
    def test_parse_packet(self):
        pkt = IP(src="192.168.1.1", dst="8.8.8.8") / TCP(sport=12345, dport=80)
        result = parse_packet(pkt)
        logging.info(f"Parsed packet result: {result}")
        self.assertIsNotNone(result)
        self.assertEqual(result["source_ip"], "192.168.1.1")

if __name__ == "__main__":
    unittest.main().
