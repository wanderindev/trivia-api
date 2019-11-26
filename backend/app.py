from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config


QUESTIONS_PER_PAGE = 10

cors = CORS()
db = SQLAlchemy()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    from models.category import Category
    from models.question import Question

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, PATCH, POST, DELETE, OPTIONS"
        )
        return response

    @app.route("/categories", methods=["GET"])
    def get_categories():
        categories = Category.list_all()
        return jsonify(
            {
                "categories": categories,
                "total_categories": len(categories),
                "success": True,
            }
        )

    @app.route("/questions", methods=["GET"])
    def get_questions():
        questions = Question.get_by_page(request, QUESTIONS_PER_PAGE)

        if len(questions) == 0:
            abort(404)

        return jsonify(
            {
                "questions": questions,
                "total_questions": len(Question.get_all()),
                "success": True,
            }
        )

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        question = Question.get_by_id(question_id)

        if question is None:
            abort(404)

        result = question.delete_record()

        if result["error"]:
            abort(500)

        questions = Question.get_by_page(request, QUESTIONS_PER_PAGE)

        return jsonify(
            {
                "deleted": question_id,
                "questions": questions,
                "total_questions": len(Question.get_all()),
                "success": True,
            }
        )

    """
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.
    """

    """
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    """

    """
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    """

    """
    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    """

    """
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    """

    """
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    """

    """
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    """

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "Not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify(
                {"success": False, "error": 422, "message": "Unprocessable"}
            ),
            422,
        )

    @app.errorhandler(500)
    def unprocessable(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 500,
                    "message": "Internal server error",
                }
            ),
            500,
        )

    return app
