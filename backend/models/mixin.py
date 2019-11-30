from datetime import date, datetime, time
from decimal import Decimal
from sqlalchemy import exc
from sqlalchemy.orm import collections
from app import db


class ModelMixin(object):
    def __iter__(self):  # pragma: no cover
        """Make model instances iterable"""
        return ((k, v) for k, v in vars(self).items() if not k.startswith("_"))

    def __repr__(self):  # pragma: no cover
        """Return a string representation of a model instance"""
        class_name = type(self).__name__
        attributes = ", ".join([f"{k!r}={v!r}" for k, v in self])

        return f"<{class_name}({attributes})>"

    # noinspection PyUnusedLocal
    def delete_record(self):
        """Delete a record from the database"""
        try:
            db.session.delete(self)
            db.session.commit()
            return {"error": False}
        except exc.SQLAlchemyError as e:  # pragma: no cover
            # print(e)
            # print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    # noinspection PyUnusedLocal
    def insert_record(self):
        """Add a new record to the database"""
        try:
            db.session.add(self)
            db.session.commit()
            return {"error": False, "id": self.id}
        except exc.SQLAlchemyError as e:  # pragma: no cover
            # print(e)
            # print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    def format(self):
        """Returns a dict representing the model instance"""
        output = {}

        for k, v in self:
            if type(v) == collections.InstrumentedList:  # pragma: no cover
                output[k] = [item.to_dict() for item in v]
            elif isinstance(v, (date, datetime, time)):  # pragma: no cover
                output[k] = v.isoformat()
            elif isinstance(v, (float, Decimal)):  # pragma: no cover
                output[k] = str(v)
            else:
                output[k] = v

        return output
