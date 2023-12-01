import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'flask_app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
UPLOAD_FOLDER = "uploads/"
MAX_CONTENT_LENGTH = 16*1024*1024 # 최대 16MB 파일 허용