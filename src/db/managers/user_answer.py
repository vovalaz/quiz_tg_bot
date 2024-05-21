from sqlalchemy.orm import Session

from db.models import UserAnswer


class UserAnswerManager:
    def __init__(self, session: Session):
        self.session = session

    def save_user_answer(self, user_id, question_id, answer_id):
        # Save user's answer
        user_answer = UserAnswer(user_id=user_id, question_id=question_id, answer_id=answer_id)
        self.session.add(user_answer)
        self.session.commit()
