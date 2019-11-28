import unittest
from .base_test import BaseTest
from models.category import Category
from models.question import Question


class TestCategory(BaseTest):
    """Integration tests for the Category model."""

    def setUp(self):
        """
        Extend the BaseTest setUp method by setting up
        two categories
        """
        super(TestCategory, self).setUp()
        with self.app_context:
            self.c_1 = Category(type="Test Category 1")
            self.c_1.insert_record()
            self.c_2 = Category(type="Test Category 2")
            self.c_2.insert_record()

    def test_get_all(self):
        """Test the get_all method for the Category model."""
        with self.app_context:
            categories = Category.get_all()
            self.assertIsNotNone(categories)
            self.assertEqual(len(categories), 2)

    def test_get_by_id(self):
        """Test the get_by_id method for the Category model."""
        with self.app_context:
            category = Category.get_by_id(self.c_1.id)
            self.assertIsNotNone(category)
            self.assertEqual(category.type, self.c_1.type)

    def test_get_ids(self):
        """Test the get_ids method for the Category model."""
        with self.app_context:
            ids = Category.get_ids()
            self.assertIsNotNone(ids)
            self.assertEqual(ids, [self.c_1.id, self.c_2.id])

    def test_get_types(self):
        """Test the get_types method for the Category model."""
        with self.app_context:
            types = Category.get_types()
            self.assertIsNotNone(types)
            self.assertEqual(types, [self.c_1.type, self.c_2.type])

    def test_list_all(self):
        """Test the list_all method for the Category model."""
        with self.app_context:
            categories = Category.list_all()
            self.assertIsNotNone(categories)
            self.assertEqual(len(categories), 2)
            self.assertEqual(
                categories,
                [
                    {"id": self.c_1.id, "type": self.c_1.type},
                    {"id": self.c_2.id, "type": self.c_2.type},
                ],
            )

    def test_to_dict(self):
        """Test the to_dict method for the Category model."""
        with self.app_context:
            categories = Category.to_dict()
            self.assertIsNotNone(categories)
            self.assertEqual(
                categories,
                {self.c_1.id: self.c_1.type, self.c_2.id: self.c_2.type},
            )


class TestQuestion(BaseTest):
    """Integration tests for the Question model."""

    def setUp(self):
        """
        Extend the BaseTest setUp method by setting up
        two categories and three questions
        """
        super(TestQuestion, self).setUp()
        with self.app_context:
            self.c_1 = Category(type="Test Category 1")
            self.c_1.insert_record()
            self.c_2 = Category(type="Test Category 2")
            self.c_2.insert_record()
            self.q_1 = Question(
                question="Test Question 1?",
                answer="Test Answer 1",
                difficulty=1,
                category_id=self.c_1.id,
            )
            self.q_1.insert_record()
            self.q_2 = Question(
                question="Test Question 2?",
                answer="Test Answer 2",
                difficulty=2,
                category_id=self.c_2.id,
            )
            self.q_2.insert_record()
            self.q_3 = Question(
                question="Test Question 3?",
                answer="Test Answer 3",
                difficulty=3,
                category_id=self.c_2.id,
            )
            self.q_3.insert_record()

    def test_get_all(self):
        """Test the get_all method for the Question model."""
        with self.app_context:
            questions = Question.get_all()
            self.assertIsNotNone(questions)
            self.assertEqual(len(questions), 3)

    def test_get_by_id(self):
        """Test the get_by_id method for the Question model."""
        with self.app_context:
            question = Question.get_by_id(self.q_1.id)
            self.assertIsNotNone(question)
            self.assertEqual(question.question, self.q_1.question)
            self.assertEqual(question.answer, self.q_1.answer)
            self.assertEqual(question.difficulty, self.q_1.difficulty)
            self.assertEqual(question.category_id, self.q_1.category_id)

    def test_get_by_category(self):
        """Test the get_by_category method for the Question model."""
        with self.app_context:
            questions = Question.get_by_category(self.c_2.id)
            self.assertIsNotNone(questions)
            self.assertEqual(len(questions), 2)
            self.assertIn(
                questions[0].format(), [self.q_2.format(), self.q_3.format()]
            )
            self.assertIn(
                questions[1].format(), [self.q_2.format(), self.q_3.format()]
            )

    def test_get_random(self):
        """Test the get_random method for the Question model."""
        with self.app_context:
            question = Question.get_random(self.c_1.id, [self.q_1.id])
            self.assertIsNone(question)
            question = Question.get_random(self.c_2.id, [self.q_2.id])
            self.assertIsNotNone(question)
            self.assertEqual(question, self.q_3.format())

    def test_search(self):
        """Test the search method for the Question model."""
        with self.app_context:
            questions = Question.search("Test Question 3?")
            self.assertIsNotNone(questions)
            self.assertEqual(questions, [self.q_3.format()])

            
if __name__ == "__main__":
    unittest.main()
