from datetime import datetime
from sqlalchemy.orm import Session

from db.models import UserQuizProgress, UserAnswer, Question, Statistics


class UserQuizProgressManager:
    def __init__(self, session: Session):
        self.session = session

    def initialize_user_quiz_progress(self, user_id, quiz_id):
        progress = UserQuizProgress(user_id=user_id, quiz_id=quiz_id, current_question_id=None)
        self.session.add(progress)
        self.session.commit()

    def get_user_quiz_progress(self, user_id):
        return self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()

    def update_user_quiz_progress(self, user_id, next_question_id):
        progress = self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()
        if progress:
            progress.current_question_id = next_question_id
            self.session.commit()

    def complete_user_quiz(self, user_id):
        progress = self.session.query(UserQuizProgress).filter_by(user_id=user_id).first()
        if not progress:
            return

        user_answers = (
            self.session.query(UserAnswer)
            .join(Question)
            .filter(UserAnswer.user_id == user_id, Question.quiz_id == progress.quiz_id)
            .all()
        )

        score = sum(answer.answer.is_correct for answer in user_answers)
        max_score = len(user_answers)

        started_at = progress.started_at
        completed_at = datetime.now()
        completion_time = (completed_at - started_at).total_seconds()

        statistics = Statistics(
            user_id=user_id,
            quiz_id=progress.quiz_id,
            score=score,
            max_score=max_score,
            completion_time=completion_time,
            completed_at=completed_at,
        )
        self.session.add(statistics)
        self.session.delete(progress)
        self.session.commit()
