from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.dirname(__file__), "../ids.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "kali-ids-secret"
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
from app import routes, socketio_events
