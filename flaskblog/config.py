import os

class Config:
    SECRET_KEY = '4ac2f50f613ac5191c8a92f174271d45c00454d0c38f17d585c42b1fa7d3fd6a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SECRET_KEY = os.environ.get('SECRET_KEY ')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')