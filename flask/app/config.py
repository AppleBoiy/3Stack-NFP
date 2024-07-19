import os


class Config:
    SECRET_KEY = os.environ.get('SECRETKEY', 'XXXXX')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    UPLOAD_FOLDER = '/uploads'
