from app import db
from .mixin import ModelMixin


class Category(db.Model, ModelMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    questions = db.relationship(
        "Question", backref="category", lazy=True, cascade="delete"
    )

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def list_all(cls):
        return [category.format() for category in cls.get_all()]
