import unittest
from app import app, db
from database.models import Alert
import logging

logging.basicConfig(filename='logs/db.log', level=logging.DEBUG)

class TestDB(unittest.TestCase):
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_save_alert(self):
        alert = Alert(identifier="test", source_ip="192.168.1.1")
        db.session.add(alert)
        db.session.commit()
        logging.debug("Alert saved to database.")
        self.assertEqual(Alert.query.count(), 1)

if __name__ == "__main__":
    unittest.main()
