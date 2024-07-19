from app import db
from sqlalchemy_serializer import SerializerMixin


class File(db.Model, SerializerMixin):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String, nullable=False)
    filepath = db.Column(db.String, nullable=False)

    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

    def __repr__(self):
        return f"<File {self.filename}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {"id": self.id, "filename": self.filename, "filepath": self.filepath}
