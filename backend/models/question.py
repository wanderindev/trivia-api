from app import db
from .mixin import ModelMixin


class Question(db.Model, ModelMixin):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("category.id"), nullable=False
    )

    def __init__(self, **kwargs):
        super(Question, self).__init__(**kwargs)

    def format(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "category": self.category,
            "difficulty": self.difficulty,
        }
