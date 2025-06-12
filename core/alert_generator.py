from database.models import Alert
import logging
logging.basicConfig(filename="logs/alert_generator.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def create_alert(alert_data):
    logging.info(f"Creating alert {alert_data[identifier]}")
    return Alert(**alert_data)
