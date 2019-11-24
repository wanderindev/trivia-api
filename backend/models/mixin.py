import sys
from sqlalchemy import exc
from flaskr import db

class ModelMixin(object):
    def __iter__(self):
        """Make model instances iterable"""
        return ((k, v) for k, v in vars(self).items() if not k.startswith("_"))

    def __repr__(self):
        """Return a string representation of a model instance"""
        class_name = type(self).__name__
        attributes = ", ".join([f"{k!r}={v!r}" for k, v in self])

        return f"<{class_name}({attributes})>"

    def delete_from_db(self):
        """Delete a record from the database"""
        try:
            db.session.delete(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    def save_to_db(self):
        """Add a record to the database"""
        try:
            db.session.add(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()
