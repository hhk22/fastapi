
import datetime
from pydantic import BaseModel
from database import get_db

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime


# db = get_db()
# question = Question(1, "subject", "This is Content", datetime.datetime.now())
# db.add(question)
# db.commit()
# db.close()
