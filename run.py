from app import app, socketio
from database.init_db import init_database
from core.capture import capture_packets
import threading
import logging
logging.basicConfig(filename="logs/run.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def start_ids():
    try:
        with app.app_context():
            init_database()
        logging.info("Starting packet capture thread")
        threading.Thread(target=capture_packets, args=("eth0",), daemon=True).start()
    except Exception as e:
        logging.error(f"Error starting IDS: {str(e)}")
        raise
if __name__ == "__main__":
    logging.info("Starting Flask-SocketIO server")
    start_ids()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
