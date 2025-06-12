import unittest
from app import app, db
from database.models import Alert
class TestDB(unittest.TestCase):
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def test_save_alert(self):
        alert = Alert(identifier="test", source_ip="192.168.1.1")
        db.session.add(alert)
        db.session.commit()
        self.assertEqual(Alert.query.count(), 1)
if __name__ == "__main__":
    unittest.main()
