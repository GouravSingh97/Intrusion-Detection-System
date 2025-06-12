from flask_socketio import emit
from app import socketio
@socketio.on("connect")
def handle_connect():
    emit("connection_status", {"status": "connected"})
def emit_alert(alert):
    socketio.emit("new_alert", {
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
    })
