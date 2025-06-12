from core.rule_engine import match_rules
import logging
logging.basicConfig(filename="logs/detector.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def detect_anomaly(alert_data):
    logging.info(f"Detecting anomaly for alert {alert_data[identifier]}")
    rule_match = match_rules(alert_data)
    if rule_match:
        alert_data["signature_id"] = rule_match["signature_id"]
        alert_data["severity"] = rule_match["severity"]
        alert_data["event_description"] = rule_match["description"]
        alert_data["intrusion_type"] = rule_match["intrusion_type"]
        alert_data["alert_message"] = rule_match["message"]
        alert_data["alert_category"] = rule_match["category"]
        logging.info(f"Anomaly detected: {alert_data[signature_id]}")
        return alert_data
    logging.info("No anomaly detected")
    return None
