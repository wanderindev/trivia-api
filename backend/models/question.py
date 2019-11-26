from app import db
from .mixin import ModelMixin


class Question(db.Model, ModelMixin):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False
    )

    def __init__(self, **kwargs):
        super(Question, self).__init__(**kwargs)

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter(cls.id == _id).one_or_none()

    @classmethod
    def get_by_page(cls, request, page_size):
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * page_size
        end = start + page_size
        return [question.format() for question in cls.get_all()[start:end]]
