

from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from questions.question_crud import get_question_list
from questions import question_schema

router = APIRouter(prefix="/api/question")


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = get_question_list(db)
    return _question_list
