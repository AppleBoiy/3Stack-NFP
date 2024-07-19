from app import db
from sqlalchemy_serializer import SerializerMixin


class Greet(db.Model, SerializerMixin):
    __tablename__ = "greetings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    msg = db.Column(db.String)

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return f"<Greet {self.msg}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {"id": self.id, "msg": self.msg}
