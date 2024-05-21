from db.orm import Orm


def init_db():
    questions_data = [
        {
            "question_text": "What is the capital of France?",
            "answers": [
                {"answer_text": "Paris", "is_correct": True},
                {"answer_text": "London", "is_correct": False},
                {"answer_text": "Berlin", "is_correct": False},
            ]
        },
        {
            "question_text": "Which planet is known as the Red Planet?",
            "answers": [
                {"answer_text": "Venus", "is_correct": False},
                {"answer_text": "Mars", "is_correct": True},
                {"answer_text": "Jupiter", "is_correct": False},
            ]
        }
    ]
    Orm.Quiz.create_quiz("General Quiz", "A quiz with general questions", questions_data)

    questions_data = [
        {
            "question_text": "Why?",
            "answers": [
                {"answer_text": "Because", "is_correct": True},
                {"answer_text": "Who asks", "is_correct": False},
                {"answer_text": "abc", "is_correct": False},
            ]
        },
        {
            "question_text": "qwerty?",
            "answers": [
                {"answer_text": "asdf", "is_correct": False},
                {"answer_text": "zxcv", "is_correct": True},
                {"answer_text": "rtyu", "is_correct": False},
                {"answer_text": "ghjk", "is_correct": False},
            ]
        },
        {
            "question_text": "Which planet is known as the Red Planet?",
            "answers": [
                {"answer_text": "Venus", "is_correct": False},
                {"answer_text": "Mars", "is_correct": True},
                {"answer_text": "Jupiter", "is_correct": False},
            ]
        }
    ]
    Orm.Quiz.create_quiz("General Quiz 2", "A quiz with general questions", questions_data)
