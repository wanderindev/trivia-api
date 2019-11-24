import os
from flaskr import create_app, db

app = create_app(os.getenv("FLASK_CONFIG") or "development")


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run()
