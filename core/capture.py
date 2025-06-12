from scapy.all import sniff
from core.parser import parse_packet
from core.detector import detect_anomaly
from database.db_utils import save_alert
from app.socketio_events import emit_alert
import os
import logging
logging.basicConfig(filename="logs/ids.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
def capture_packets(interface="eth0"):
    if os.geteuid() != 0:
        raise PermissionError("Root privileges required")
    try:
        sniff(iface=interface, prn=lambda pkt: process_packet(pkt), store=False)
    except Exception as e:
        logging.error(f"Packet capture failed: {str(e)}")
        raise
def process_packet(packet):
    try:
        alert_data = parse_packet(packet)
        if alert_data:
            alert = detect_anomaly(alert_data)
            if alert:
                save_alert(alert)
                emit_alert(alert)
    except Exception as e:
        logging.error(f"Error processing packet: {str(e)}")
