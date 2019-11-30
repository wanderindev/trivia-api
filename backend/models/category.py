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
    def get_all(cls) -> list:
        """
        Return all Category records ordered by id.
        
        :return: a list of Category objects
        """
        return cls.query.order_by(cls.id).all()

    @classmethod
    def get_by_id(cls, _id: int) -> object:
        """
        Return the Category object identified by _id.

        :param _id: id for the Category object
        :type _id: int
        :return: instance of Category
        """
        return cls.query.filter(cls.id == _id).one_or_none()

    @classmethod
    def get_ids(cls) -> list:
        """
        Return a list of all Category ids.

        :return: list of int with all Category ids
        """
        return [category.id for category in cls.get_all()]

    @classmethod
    def get_types(cls) -> list:
        """
        Return a list of all Category types.

        :return: list of str with all Category types
        """
        return [category.type for category in cls.get_all()]

    @classmethod
    def list_all(cls) -> list:
        """
        Return a list of dict.  Each dict represent a Category. The
        list contains all Category

        :return: list of dict with all Category
        """
        return [category.format() for category in cls.get_all()]

    @classmethod
    def to_dict(cls) -> dict:
        """
        Return a dict representing all Category.  Each key is a Category
        id cast as a str. Each value is the Category type.

        :return: dict with all Category id:type
        """
        return dict(zip(cls.get_ids(), cls.get_types()))
