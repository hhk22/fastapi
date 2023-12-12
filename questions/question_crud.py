
from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_time.desc())\
        .all()
    return question_list