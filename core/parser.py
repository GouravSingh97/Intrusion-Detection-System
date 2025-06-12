from scapy.all import IP, TCP, UDP, Ether
from core.geo import get_geolocation
from core.resolver import resolve_hostname, get_mac
import hashlib
import uuid
import logging
logging.basicConfig(filename="logs/parser.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
def parse_packet(packet):
    logging.debug("Parsing new packet")
    if not packet.haslayer(IP):
        logging.debug("No IP layer found")
        return None
    ip_layer = packet[IP]
    alert = {
        "identifier": str(uuid.uuid4()),
        "source_ip": ip_layer.src,
        "destination_ip": ip_layer.dst,
        "source_port": None,
        "destination_port": None,
        "protocol": ip_layer.proto,
        "timestamp": packet.time,
        "alert_type": "Network",
        "event_id": str(uuid.uuid4()),
        "payload": None,
        "user_agent": None,
        "action_taken": "Logged",
        "signature_id": None,
        "severity": "Low",
        "event_description": "Network packet detected",
        "intrusion_type": None,
        "file_hash": None,
        "payload_length": len(packet),
        "protocol_flags": None,
        "connection_id": str(uuid.uuid4()),
        "alert_message": "Packet captured",
        "flow_direction": "Inbound",
        "alert_category": "Network",
        "source_mac": None,
        "destination_mac": None,
        "host_name": None,
        "geolocation": get_geolocation(ip_layer.src),
        "bytes_transferred": len(packet),
        "packet_count": 1,
        "application_layer_data": None,
        "alert_source": "Scapy",
        "hostname_source": resolve_hostname(ip_layer.src),
        "hostname_destination": resolve_hostname(ip_layer.dst)
    }
    logging.debug(f"Initial alert created: {alert[identifier]}")
    if packet.haslayer(Ether):
        ether_layer = packet[Ether]
        alert["source_mac"] = ether_layer.src
        alert["destination_mac"] = ether_layer.dst
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        alert["source_port"] = tcp_layer.sport
        alert["destination_port"] = tcp_layer.dport
        alert["protocol_flags"] = str(tcp_layer.flags)
        if packet.haslayer("Raw"):
            alert["payload"] = packet["Raw"].load.hex()
            alert["file_hash"] = hashlib.md5(packet["Raw"].load).hexdigest()
            if b"HTTP" in packet["Raw"].load:
                alert["application_layer_data"] = packet["Raw"].load.decode(errors="ignore")
                alert["user_agent"] = extract_user_agent(packet["Raw"].load)
    elif packet.haslayer(UDP):
        udp_layer = packet[UDP]
        alert["source_port"] = udp_layer.sport
        alert["destination_port"] = udp_layer.dport
        if packet.haslayer("Raw"):
            alert["payload"] = packet["Raw"].load.hex()
            alert["file_hash"] = hashlib.md5(packet["Raw"].load).hexdigest()
    logging.debug(f"Final alert: {alert}")
    return alert
def extract_user_agent(raw_data):
    try:
        data = raw_data.decode(errors="ignore")
        for line in data.split("\n"):
            if "User-Agent:" in line:
                return line.split("User-Agent:")[1].strip()
    except Exception as e:
        logging.error(f"Error extracting user agent: {str(e)}")
    return None
