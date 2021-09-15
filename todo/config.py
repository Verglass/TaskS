import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.environ.get("TASKS_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("USER_EMAIL")
    MAIL_PASSWORD = os.environ.get("USER_PASS")
