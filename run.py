from app import app, socketio
from database.init_db import init_database
from core.capture import capture_packets
import threading
import logging
import os
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
def start_ids():
    try:
        with app.app_context():
            init_database()
            logger.info("Database initialized successfully.")
        logger.info("Starting packet capture thread...")
        threading.Thread(target=capture_packets, args=("eth0",), daemon=True).start()
    except Exception as e:
        logger.error(f"Error starting IDS: {str(e)}", exc_info=True)
        raise
if __name__ == "__main__":
    logger.info("Starting Flask-SocketIO server on http://0.0.0.0:5000")
    start_ids()
    try:
        socketio.run(app, host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        logger.error(f"Failed to start Flask server: {str(e)}", exc_info=True)
