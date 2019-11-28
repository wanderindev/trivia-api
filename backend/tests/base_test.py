from unittest import TestCase
from app import create_app, db
from models.category import Category
from models.question import Question

app = create_app("testing")


class BaseTest(TestCase):
    """
    Base class which is inherited by all
    system test classes.
    """

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        """Create all db tables before each test."""
        self.client = app.test_client
        self.app_context = app.app_context()

        with self.app_context:
            db.create_all()

    def tearDown(self):
        """Clear db tables after each test"""
        with self.app_context:
            self.clear_db()

    @staticmethod
    def clear_db():
        """Delete all rows in all tables"""
        db.session.remove()
        Question.query.delete()
        Category.query.delete()
        db.session.commit()
