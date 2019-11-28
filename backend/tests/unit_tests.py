import unittest
from unittest import TestCase
from models.category import Category
from models.question import Question


class TestCategory(TestCase):
    """Unit tests for the Category model."""

    def test_init(self):
        """Test the __init__ method for the Category class."""
        self.c = Category(type="Test Category")
        self.assertEqual(self.c.type, "Test Category")


class TestQuestion(TestCase):
    """Unit tests for the Question model."""

    def test_init(self):
        """Test the __init__ method for the Question class."""
        self.q = Question(
            question="Test Question?",
            answer="Test Answer",
            difficulty="1",
            category_id="2",
        )
        self.assertEqual(self.q.question, "Test Question?")
        self.assertEqual(self.q.answer, "Test Answer")
        self.assertEqual(int(self.q.difficulty), 1)
        self.assertEqual(int(self.q.category_id), 2)


if __name__ == "__main__":
    unittest.main()
