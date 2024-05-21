from sqlalchemy.orm import Session

from db.models import Answer


class AnswerManager:
    def __init__(self, session: Session):
        self.session = session

    def get_answers_by_question_id(self, question_id):
        # Fetch all answers for a question
        return self.session.query(Answer).filter_by(question_id=question_id).all()

    def get_answer_by_text(self, question_id, answer_text):
        # Fetch answer by text for a given question
        return self.session.query(Answer).filter_by(question_id=question_id, answer_text=answer_text).first()
