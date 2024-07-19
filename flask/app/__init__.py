import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__, static_folder="static")
app.config.from_object(Config)

db = SQLAlchemy()

api = Api(app)
db.init_app(app)

jwt = JWTManager(app)

CORS(
    app,
    supports_credentials=True,
    resources={r"*": {"origins": "*"}},
    expose_headers="Authorization,Content-Type,Authentication",
)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


from .models.token_blocklist import TokenBlocklist


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = TokenBlocklist.query.filter_by(jti=jti).scalar()
    return token is not None


from app.models.user import User


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

with app.app_context():
    db.create_all()

from app._api.ping import ping_ns
from app._api.greets import greet_ns
from app._api.file import file_ns
from app._api.user import user_ns

api.add_namespace(ping_ns)
api.add_namespace(greet_ns)
api.add_namespace(file_ns)
api.add_namespace(user_ns)
