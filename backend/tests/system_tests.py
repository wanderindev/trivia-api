import json
import unittest
from models.category import Category
from models.question import Question
from tests.base_test import BaseTest


class TestCategoryResource(BaseTest):
    """System tests for the Category resources."""

    def setUp(self):
        """
        Extend the BaseTest setUp method by inserting  two
        categories into the database.
        """
        super(TestCategoryResource, self).setUp()
        with self.app_context:
            self.c_1 = Category(type="Test Category 1")
            self.c_1.insert_record()
            self.c_2 = Category(type="Test Category 2")
            self.c_2.insert_record()

    def test_get_categories(self):
        """
        Test that a GET request to the /categories endpoint returns
        the correct response when there are categories in the database.
        """
        with self.client as c:
            result = json.loads(
                c.get(
                    "/categories", headers={"Content-Type": "application/json"}
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["categories"],
                {
                    str(self.c_1.format()["id"]): self.c_1.format()["type"],
                    str(self.c_2.format()["id"]): self.c_2.format()["type"],
                },
            )

    def test_get_categories_empty(self):
        """
        Test that a GET request to the /categories endpoint returns
        the correct response when there are no categories in the
        database.
        """
        with self.app_context:
            self.c_1.delete_record()
            self.c_2.delete_record()
        with self.client as c:
            result = json.loads(
                c.get(
                    "/categories", headers={"Content-Type": "application/json"}
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 404)
            self.assertEqual(result["message"], "Not found")


class TestQuestionResource(BaseTest):
    """System tests for the Question resources."""

    def setUp(self):
        """
        Extend the BaseTest setUp method by inserting  two
        categories into the database and twelve questions.
        """
        super(TestQuestionResource, self).setUp()
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

            self.q_4 = Question(
                question="Test Question 4?",
                answer="Test Answer 4",
                difficulty=1,
                category_id=self.c_1.id,
            )
            self.q_4.insert_record()
            self.q_5 = Question(
                question="Test Question 5?",
                answer="Test Answer 5",
                difficulty=2,
                category_id=self.c_2.id,
            )
            self.q_5.insert_record()
            self.q_6 = Question(
                question="Test Question 6?",
                answer="Test Answer 6",
                difficulty=3,
                category_id=self.c_2.id,
            )
            self.q_6.insert_record()

            self.q_7 = Question(
                question="Test Question 7?",
                answer="Test Answer 7",
                difficulty=1,
                category_id=self.c_1.id,
            )
            self.q_7.insert_record()
            self.q_8 = Question(
                question="Test Question 8?",
                answer="Test Answer 8",
                difficulty=2,
                category_id=self.c_2.id,
            )
            self.q_8.insert_record()
            self.q_9 = Question(
                question="Test Question 9?",
                answer="Test Answer 9",
                difficulty=3,
                category_id=self.c_2.id,
            )
            self.q_9.insert_record()

            self.q_10 = Question(
                question="Test Question 10?",
                answer="Test Answer 10",
                difficulty=1,
                category_id=self.c_1.id,
            )
            self.q_10.insert_record()
            self.q_11 = Question(
                question="Test Question 11?",
                answer="Test Answer 11",
                difficulty=2,
                category_id=self.c_2.id,
            )
            self.q_11.insert_record()
            self.q_12 = Question(
                question="Test Question 12?",
                answer="Test Answer 12",
                difficulty=3,
                category_id=self.c_2.id,
            )
            self.q_12.insert_record()

    def test_get_questions_no_page(self):
        """
        Test that a GET request to the /questions endpoint returns
        the correct response when there are questions in the database
        and no page in url parameters.
        """
        with self.client as c:
            result = json.loads(
                c.get(
                    "/questions", headers={"Content-Type": "application/json"}
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["categories"],
                {
                    str(self.c_1.format()["id"]): self.c_1.format()["type"],
                    str(self.c_2.format()["id"]): self.c_2.format()["type"],
                },
            )
            self.assertEqual(
                result["questions"],
                [question.format() for question in Question.get_all()[0:10]],
            )
            self.assertEqual(
                result["total_questions"], len(Question.get_all())
            )

    def test_get_questions_with_page(self):
        """
        Test that a GET request to the /questions endpoint returns
        the correct response when there are questions in the database
        and a page in url parameters.
        """
        with self.client as c:
            result = json.loads(
                c.get(
                    "/questions?page=2",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["categories"],
                {
                    str(self.c_1.format()["id"]): self.c_1.format()["type"],
                    str(self.c_2.format()["id"]): self.c_2.format()["type"],
                },
            )
            self.assertEqual(
                result["questions"],
                [question.format() for question in Question.get_all()[10:20]],
            )
            self.assertEqual(
                result["total_questions"], len(Question.get_all())
            )

    def test_get_questions_invalid_page(self):
        """
        Test that a GET request to the /questions endpoint returns
        the correct response when there are questions in the database
        and an invalid page in url parameters.
        """
        with self.client as c:
            result = json.loads(
                c.get(
                    "/questions?page=3",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 404)
            self.assertEqual(result["message"], "Not found")

    def test_delete_question(self):
        """
        Test that a DELETE request to the /questions/<int:question_id>
        endpoint returns the correct response when the question is
        in the database.
        """
        with self.client as c:
            question_id = self.q_12.format()["id"]
            result = json.loads(
                c.delete(
                    f"/questions/{question_id}",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(result["deleted"], question_id)
            self.assertEqual(
                result["questions"],
                [question.format() for question in Question.get_all()[0:10]],
            )
            self.assertEqual(
                result["total_questions"], len(Question.get_all())
            )

    def test_delete_question_not_found(self):
        """
        Test that a DELETE request to the /questions/<int:question_id>
        endpoint returns the correct response when the question is NOT
        in the database.
        """
        with self.client as c:
            question_id = 100000000
            result = json.loads(
                c.delete(
                    f"/questions/{question_id}",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 404)
            self.assertEqual(result["message"], "Not found")

    def test_post_question_valid(self):
        """
        Test that a POST request to the /questions endpoint returns
        the correct response for a valid question.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    "/questions",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(
                        {
                            "question": "Test Question 13?",
                            "answer": "Test Answer 13",
                            "difficulty": 5,
                            "category_id": self.c_1.format()["id"],
                        }
                    ),
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["created"],
                Question.search("Test Question 13?")[0]["id"],
            )
            self.assertEqual(
                result["questions"],
                [question.format() for question in Question.get_all()[0:10]],
            )
            self.assertEqual(
                result["total_questions"], len(Question.get_all())
            )

    def test_post_question_invalid(self):
        """
        Test that a POST request to the /questions endpoint returns
        the correct response for a invalid question.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    "/questions",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(
                        {
                            "question": "Test Question 13?",
                            "answer": "Test Answer 13",
                            "difficulty": 5,
                            "category_id": 0,
                        }
                    ),
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 500)
            self.assertEqual(result["message"], "Internal server error")

    def test_search_question_valid(self):
        """
        Test that a POST request to the /questions/search endpoint returns
        the correct response for a valid search_term.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    "/questions/search",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps({"search_term": "Question 1"}),
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["questions"],
                [
                    question.format()
                    for question in [self.q_1, self.q_10, self.q_11, self.q_12]
                ],
            )
            self.assertEqual(result["total_questions"], 4)

    def test_search_question_invalid(self):
        """
        Test that a POST request to the /questions/search endpoint returns
        the correct response for a invalid search_term.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    "/questions/search",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps({"search_term": "Hello World!"}),
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 404)
            self.assertEqual(result["message"], "Not found")

    def test_get_questions_by_category_valid(self):
        """
        Test that a GET request to the /categories/<int:category_id>/questions
        endpoint returns the correct response when there are questions in the
        database for the chosen category.
        """
        with self.client as c:
            category_id = self.c_1.format()["id"]
            result = json.loads(
                c.get(
                    f"/categories/{category_id}/questions",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["current_category"],
                Category.get_by_id(category_id).type,
            )
            self.assertEqual(
                result["questions"],
                [
                    question.format()
                    for question in Question.get_by_category(category_id)[0:10]
                ],
            )
            self.assertEqual(
                result["total_questions"],
                len(Question.get_by_category(category_id)),
            )

    def test_get_questions_by_category_invalid(self):
        """
        Test that a GET request to the /categories/<int:category_id>/questions
        endpoint returns the correct response when there are NO questions in
        the database for the chosen category.
        """
        with self.client as c:
            category_id = 10000000
            result = json.loads(
                c.get(
                    f"/categories/{category_id}/questions",
                    headers={"Content-Type": "application/json"},
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 404)
            self.assertEqual(result["message"], "Not found")

    def test_quizz_valid(self):
        """
        Test that a POST request to the /quizzes endpoint returns the
        correct response when there are questions in the database for
        the chosen category.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    f"/quizzes",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(
                        {
                            "previous_questions": [],
                            "quiz_category": self.c_1.format(),
                        }
                    ),
                ).data
            )
            self.assertTrue(result["success"])
            self.assertEqual(
                result["question"]["category_id"], self.c_1.format()["id"],
            )

    def test_quizz_no_more_questions(self):
        """
        Test that a POST request to the /quizzes endpoint returns the
        correct response when there are NO more questions in the database for
        the chosen category.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    f"/quizzes",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(
                        {
                            "previous_questions": [],
                            "quiz_category": {
                                "id": 100000,
                                "type": "New category",
                            },
                        }
                    ),
                ).data
            )
            self.assertTrue(result["success"])

    def test_quizz_no_category(self):
        """
        Test that a POST request to the /quizzes endpoint returns the
        correct response when the payload does not contain a category.
        """
        with self.client as c:
            result = json.loads(
                c.post(
                    f"/quizzes",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps({"previous_questions": []}),
                ).data
            )
            self.assertFalse(result["success"])
            self.assertEqual(result["error"], 400)
            self.assertEqual(result["message"], "Bad request")


if __name__ == "__main__":
    unittest.main()
