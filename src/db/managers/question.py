from sqlalchemy.orm import Session

from db.models import Question, UserQuizProgress


class QuestionManager:
    def __init__(self, session: Session):
        self.session = session

    def get_question_by_id(self, question_id):
        # Fetch question by id
        return self.session.query(Question).filter_by(id=question_id).first()

    def get_next_question(self, user_quiz_progress: UserQuizProgress):
        # Get next question based on user progress
        quiz_id = user_quiz_progress.quiz_id
        current_question_id = user_quiz_progress.current_question_id
        questions = self.session.query(Question).filter_by(quiz_id=quiz_id).order_by(Question.id).all()
        current_index = next((i for i, q in enumerate(questions) if q.id == current_question_id), -1)
        next_index = current_index + 1
        return questions[next_index] if next_index < len(questions) else None
