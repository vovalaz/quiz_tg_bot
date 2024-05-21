from sqlalchemy.orm import Session

from db.models import UserQuizProgress


class UserQuizProgressManager:
    def __init__(self, session: Session):
        self.session = session

    def initialize_user_quiz_progress(self, user_id, quiz_id):
        # Initialize user's quiz progress
        progress = UserQuizProgress(user_id=user_id, quiz_id=quiz_id, current_question_id=None)
        self.session.add(progress)
        self.session.commit()

    def get_user_quiz_progress(self, user_id):
        # Fetch user's current quiz progress
        return self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()

    def update_user_quiz_progress(self, user_id, next_question_id):
        # Update user's current question in progress
        progress = self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()
        if progress:
            progress.current_question_id = next_question_id
            self.session.commit()

    def complete_user_quiz(self, user_id):
        # Mark quiz as completed and save statistics
        progress = self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()
        if progress:
            self.session.delete(progress)
            self.session.commit()
        # Further implementation to save quiz completion statistics
