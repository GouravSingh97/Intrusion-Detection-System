from app import db
from database.models import Alert
import logging
logging.basicConfig(filename="logs/db.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
def init_database():
    try:
        db.create_all()
        logging.info("Database initialized successfully")
    except Exception as e:
        logging.error(f"Database initialization error: {str(e)}")
        raise
