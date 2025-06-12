class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///ids.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "kali-ids-secret"
    INTERFACE = "eth0"
