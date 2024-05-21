from typing import Any

from sqlalchemy.orm import Session

from db.models import Answer, Question, Quiz


class QuizManager:
    def __init__(self, session: Session):
        self.session = session

    def get_quiz_by_title(self, title) -> Quiz:
        return self.session.query(Quiz).filter_by(title=title).first()

    def get_quiz_by_id(self, id) -> Quiz:
        return self.session.query(Quiz).filter_by(id=id).first()

    def create_quiz(self, title: str, description: str, questions_data: list[dict[str, Any]]):
        """
        Example:
        questions_data = [
            {
                "question_text": "What is the capital of France?",
                "answers": [
                    {"answer_text": "Paris", "is_correct": True},
                    {"answer_text": "London", "is_correct": False},
                    {"answer_text": "Berlin", "is_correct": False},
                ]
            },
            ...
        ]
        """

        quiz = Quiz(title=title, description=description)
        self.session.add(quiz)
        self.session.commit()

        for question_data in questions_data:
            question = Question(quiz_id=quiz.id, question_text=question_data["question_text"])
            self.session.add(question)
            self.session.commit()

            for answer_data in question_data["answers"]:
                answer = Answer(
                    question_id=question.id,
                    answer_text=answer_data["answer_text"],
                    is_correct=answer_data["is_correct"],
                )
                self.session.add(answer)

        self.session.commit()

    def get_all_quizzes(self) -> list[Quiz]:
        return self.session.query(Quiz).all()
