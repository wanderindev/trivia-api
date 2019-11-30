import random
from flask import request
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
    def get_all(cls) -> list:
        """
        Return all Question records ordered by id.

        :return: a list of Question objects
        """
        return cls.query.order_by(cls.id).all()

    @classmethod
    def get_by_id(cls, _id) -> object:
        """
        Return the Question object identified by _id.

        :param _id: id for the Question object
        :type _id: int
        :return: instance of Question
        """
        return cls.query.filter(cls.id == _id).one_or_none()

    @classmethod
    def get_by_category(cls, category_id: int) -> list:
        """
        Return a list of all Question objects that belong to a
        given Category.

        :param category_id: the category id
        :type category_id: int
        :return: list of Question objects
        """
        if category_id == 0:
            return cls.query.all()
        return cls.query.filter(cls.category_id == category_id).all()

    @classmethod
    def get_by_category_by_page(
        cls, category_id: int, _request: request, page_size: int
    ) -> list:
        """
        Return a list of dict.  Each dict represents a Question object for a
        give category. The list is a subset of all the Question object of
        size page_size.

        :param category_id: the category id
        :type category_id: int
        :param _request: a Flask request object
        :type _request: object
        :param page_size: the max number of Questions to include in the list
        :type page_size: int
        :return: a list of dict
        """
        page = _request.args.get("page", 1, type=int)
        start = (page - 1) * page_size
        end = start + page_size
        return [
            question.format()
            for question in cls.get_by_category(category_id)[start:end]
        ]

    @classmethod
    def get_by_page(cls, _request: request, page_size: int) -> list:
        """
        Return a list of dict.  Each dict represents a Question object.
        The list is a subset of all the Question object of size page_size.

        :param _request: a Flask request object
        :type _request: object
        :param page_size: the max number of Questions to include in the list
        :type page_size: int
        :return: a list of dict
        """
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * page_size
        end = start + page_size
        return [question.format() for question in cls.get_all()[start:end]]

    @classmethod
    def get_random(
        cls, category_id: int, previous_questions: list
    ) -> dict or None:
        """
        Return a random Question as a dict, which is not included in the
        previous_questions list and belonging to the given category.

        :param category_id: the category id
        :type category_id: int
        :param previous_questions: list of previously returned questions
        :type previous_questions: list
        :return: a dict representing a Question
        """
        questions = cls.get_by_category(category_id)
        new_questions = [
            question.format()
            for question in questions
            if question.format()["id"] not in previous_questions
        ]

        if len(new_questions) == 0:
            return None
        return random.choice(new_questions)

    @classmethod
    def search(cls, search_term: str) -> list:
        """
        Return a list of dict representing Questions which include in
        their question property the case insensitive search_term.

        :param search_term: the term to search for in Question.question
        :type search_term: str
        :return: list of Question dicts
        """
        questions = cls.query.filter(
            cls.question.ilike(f"%{search_term}%")
        ).all()
        return [question.format() for question in questions]
