import bcrypt
from app import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {'id': self.id, 'username': self.username}

    def __repr__(self):
        return f'<User {self.username}>'

    # check user exists or not
    @staticmethod
    def is_user_exist(username):
        return User.query.filter_by(username=username).first() is not None
