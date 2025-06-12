import socket
import subprocess
import logging
logging.basicConfig(filename="logs/resolver.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception as e:
        logging.error(f"Hostname resolution error for IP {ip}: {str(e)}")
        return "Unknown"
def get_mac(ip):
    try:
        result = subprocess.check_output(["arp", "-n", ip]).decode()
        for line in result.split("\n"):
            if ip in line:
                return line.split()[3]
    except Exception as e:
        logging.error(f"MAC resolution error for IP {ip}: {str(e)}")
        return "Unknown"
