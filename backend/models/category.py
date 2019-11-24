from app import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    questions = db.relationship(
        "Question", backref="category", lazy=True, cascade="delete"
    )

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)

    def format(self):
        return {"id": self.id, "type": self.type}
