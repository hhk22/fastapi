

from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from questions.question_crud import get_question_list
from questions import question_schema, question_crud

router = APIRouter(prefix="/api/question")


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = get_question_list(db)
    return _question_list


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id)
    return question
