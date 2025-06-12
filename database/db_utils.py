from app import db
from database.models import Alert
from datetime import datetime
import logging
logging.basicConfig(filename="logs/db.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
def save_alert(alert_data):
    try:
        alert_data["timestamp"] = datetime.fromtimestamp(alert_data["timestamp"])
        alert = Alert(**alert_data)
        db.session.add(alert)
        db.session.commit()
        logging.info(f"Alert saved: {alert_data[identifier]}")
        return alert
    except Exception as e:
        logging.error(f"Error saving alert {alert_data[identifier]}: {str(e)}")
        db.session.rollback()
        raise
