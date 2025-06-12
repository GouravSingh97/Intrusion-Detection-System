import json
import re
import os
import logging
logging.basicConfig(filename="logs/rules.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
rules_path = os.path.join(os.path.dirname(__file__), "../rules/rules.json")
with open(rules_path) as f:
    RULES = json.load(f)
def match_rules(alert_data):
    logging.info(f"Matching rules for alert {alert_data[identifier]}")
    for rule in RULES:
        if rule["protocol"] == alert_data["protocol"]:
            if "payload_pattern" in rule and alert_data["payload"]:
                if re.search(rule["payload_pattern"], alert_data["payload"]):
                    logging.info(f"Rule matched: {rule[signature_id]}")
                    return rule
            if "port" in rule and (alert_data["source_port"] == rule["port"] or alert_data["destination_port"] == rule["port"]):
                logging.info(f"Rule matched: {rule[signature_id]}")
                return rule
    logging.info("No rule matched")
    return None
