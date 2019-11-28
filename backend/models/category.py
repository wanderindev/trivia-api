from app import db
from .mixin import ModelMixin
from .question import Question


class Category(db.Model, ModelMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    questions = db.relationship(
        Question, backref="category", lazy=True, cascade="delete"
    )

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter(cls.id == _id).one_or_none()

    @classmethod
    def get_ids(cls):
        return [category.id for category in cls.get_all()]

    @classmethod
    def get_types(cls):
        return [category.type for category in cls.get_all()]

    @classmethod
    def list_all(cls):
        return [category.format() for category in cls.get_all()]

    @classmethod
    def to_dict(cls):
        return dict(zip(cls.get_ids(), cls.get_types()))
