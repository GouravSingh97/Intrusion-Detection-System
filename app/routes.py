from flask import render_template, jsonify, request, Response
from app import app, db
from database.models import Alert
from datetime import datetime
import os
import logging

LOG_DIR = "logs"
logging.basicConfig(filename=os.path.join(LOG_DIR, "app.log"), level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Homepage: Render Dashboard Template
@app.route("/")
def dashboard():
    try:
        return render_template("dashboard.html")
    except Exception as e:
        logging.error(f"Error rendering dashboard: {str(e)}")
        return "Dashboard error", 500

# ✅ List all log files
@app.route("/log_files")
def log_files():
    try:
        files = [f for f in os.listdir(LOG_DIR) if f.endswith(".log")]
        return jsonify({"files": files})
    except Exception as e:
        logging.error(f"Error fetching log files: {str(e)}")
        return jsonify({"error": "Failed to list log files"}), 500

# ✅ View a specific log file's last 200 lines
@app.route("/view_log")
def view_log():
    try:
        log_file = request.args.get("log")
        if not log_file or ".." in log_file:
            return jsonify({"error": "Invalid file name"}), 400

        file_path = os.path.join(LOG_DIR, log_file)
        if not os.path.exists(file_path):
            return jsonify({"error": "Log file not found"}), 404

        with open(file_path, "r") as f:
            lines = f.readlines()[-200:]
        return jsonify({"content": lines})
    except Exception as e:
        logging.error(f"Error reading log file: {str(e)}")
        return jsonify({"error": "Failed to read log file"}), 500

# ✅ History route with protocol and date filters
@app.route("/history")
def history():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = 50
        protocol = request.args.get("protocol")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        query = Alert.query

        if protocol:
            query = query.filter(Alert.protocol.ilike(protocol))

        if start_date and end_date:
            try:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                end = datetime.strptime(end_date, "%Y-%m-%d")
                query = query.filter(Alert.timestamp.between(start, end))
            except ValueError:
                logging.warning("Invalid date format provided.")

        alerts = query.order_by(Alert.timestamp.desc()).paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({
            "alerts": [{
                "identifier": alert.identifier,
                "source_ip": alert.source_ip,
                "destination_ip": alert.destination_ip,
                "source_port": alert.source_port,
                "destination_port": alert.destination_port,
                "protocol": alert.protocol,
                "timestamp": alert.timestamp.isoformat(),
                "alert_type": alert.alert_type,
                "event_id": alert.event_id,
                "payload": alert.payload,
                "user_agent": alert.user_agent,
                "action_taken": alert.action_taken,
                "signature_id": alert.signature_id,
                "severity": alert.severity,
                "event_description": alert.event_description,
                "intrusion_type": alert.intrusion_type,
                "file_hash": alert.file_hash,
                "payload_length": alert.payload_length,
                "protocol_flags": alert.protocol_flags,
                "connection_id": alert.connection_id,
                "alert_message": alert.alert_message,
                "flow_direction": alert.flow_direction,
                "alert_category": alert.alert_category,
                "source_mac": alert.source_mac,
                "destination_mac": alert.destination_mac,
                "host_name": alert.host_name,
                "geolocation": alert.geolocation,
                "bytes_transferred": alert.bytes_transferred,
                "packet_count": alert.packet_count,
                "application_layer_data": alert.application_layer_data,
                "alert_source": alert.alert_source,
                "hostname_source": alert.hostname_source,
                "hostname_destination": alert.hostname_destination
            } for alert in alerts.items],
            "total_pages": alerts.pages,
            "current_page": alerts.page
        })
    except Exception as e:
        logging.error(f"Error in /history: {str(e)}")
        return jsonify({"error": "Failed to fetch alerts"}), 500

# ✅ Export filtered alerts as CSV
@app.route("/export_csv")
def export_csv():
    try:
        protocol = request.args.get("protocol")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        query = Alert.query

        if protocol:
            query = query.filter(Alert.protocol.ilike(protocol))

        if start_date and end_date:
            try:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                end = datetime.strptime(end_date, "%Y-%m-%d")
                query = query.filter(Alert.timestamp.between(start, end))
            except ValueError:
                logging.warning("Invalid date format for CSV export")

        alerts = query.order_by(Alert.timestamp.desc()).all()

        def generate():
            # CSV Header
            yield ','.join([
                "timestamp", "source_ip", "destination_ip", "protocol", "alert_message"
            ]) + "\n"
            for alert in alerts:
                yield ','.join([
                    alert.timestamp.isoformat(),
                    alert.source_ip,
                    alert.destination_ip,
                    alert.protocol,
                    alert.alert_message.replace(',', ' ')
                ]) + "\n"

        return Response(generate(), mimetype='text/csv',
                        headers={"Content-Disposition": "attachment;filename=alerts.csv"})
    except Exception as e:
        logging.error(f"Error in /export_csv: {str(e)}")
        return jsonify({"error": "CSV export failed"}), 500
