from db.orm import Orm


def init_db():
    # History of Ukraine Quiz
    history_ukraine_questions = [
        {
            "question_text": "Who was the first president of independent Ukraine?",
            "answers": [
                {"answer_text": "Leonid Kravchuk", "is_correct": True},
                {"answer_text": "Viktor Yanukovych", "is_correct": False},
                {"answer_text": "Petro Poroshenko", "is_correct": False},
            ],
        },
        {
            "question_text": "In which year did Ukraine declare its independence from the Soviet Union?",
            "answers": [
                {"answer_text": "1990", "is_correct": False},
                {"answer_text": "1991", "is_correct": True},
                {"answer_text": "1992", "is_correct": False},
            ],
        },
        {
            "question_text": "What was the name of the medieval state that existed in Ukraine from the 9th to the 13th century?",
            "answers": [
                {"answer_text": "Kievan Rus'", "is_correct": True},
                {"answer_text": "Galicia-Volhynia", "is_correct": False},
                {"answer_text": "Cossack Hetmanate", "is_correct": False},
            ],
        },
    ]
    Orm.Quiz.create_quiz(
        "History of Ukraine Quiz", "A quiz with questions about the history of Ukraine", history_ukraine_questions
    )

    # Math Quiz
    math_questions = [
        {
            "question_text": "What is the derivative of x^2?",
            "answers": [
                {"answer_text": "2x", "is_correct": True},
                {"answer_text": "x", "is_correct": False},
                {"answer_text": "x^2", "is_correct": False},
            ],
        },
        {
            "question_text": "Solve for x: 2x + 3 = 7",
            "answers": [
                {"answer_text": "x = 2", "is_correct": True},
                {"answer_text": "x = 1", "is_correct": False},
                {"answer_text": "x = 3", "is_correct": False},
            ],
        },
        {
            "question_text": "What is the value of the integral of 1/x dx?",
            "answers": [
                {"answer_text": "ln|x| + C", "is_correct": True},
                {"answer_text": "x + C", "is_correct": False},
                {"answer_text": "1/x + C", "is_correct": False},
            ],
        },
    ]
    Orm.Quiz.create_quiz("Math Quiz", "A quiz with math questions", math_questions)

    # Astronomy Quiz
    astronomy_questions = [
        {
            "question_text": "Which planet in our solar system has the most moons?",
            "answers": [
                {"answer_text": "Jupiter", "is_correct": True},
                {"answer_text": "Saturn", "is_correct": False},
                {"answer_text": "Mars", "is_correct": False},
            ],
        },
        {
            "question_text": "What is the name of the galaxy that contains our Solar System?",
            "answers": [
                {"answer_text": "Milky Way", "is_correct": True},
                {"answer_text": "Andromeda", "is_correct": False},
                {"answer_text": "Triangulum", "is_correct": False},
            ],
        },
        {
            "question_text": "Who was the first person to walk on the Moon?",
            "answers": [
                {"answer_text": "Neil Armstrong", "is_correct": True},
                {"answer_text": "Buzz Aldrin", "is_correct": False},
                {"answer_text": "Yuri Gagarin", "is_correct": False},
            ],
        },
    ]
    Orm.Quiz.create_quiz("Astronomy Quiz", "A quiz with astronomy questions", astronomy_questions)

    # Geography of Ukraine Quiz
    geography_ukraine_questions = [
        {
            "question_text": "What is the capital of Ukraine?",
            "answers": [
                {"answer_text": "Kyiv", "is_correct": True},
                {"answer_text": "Lviv", "is_correct": False},
                {"answer_text": "Kharkiv", "is_correct": False},
            ],
        },
        {
            "question_text": "Which river is the longest in Ukraine?",
            "answers": [
                {"answer_text": "Dnipro", "is_correct": True},
                {"answer_text": "Dniester", "is_correct": False},
                {"answer_text": "Southern Bug", "is_correct": False},
            ],
        },
        {
            "question_text": "What is the highest mountain in Ukraine?",
            "answers": [
                {"answer_text": "Hoverla", "is_correct": True},
                {"answer_text": "Petros", "is_correct": False},
                {"answer_text": "Pip Ivan", "is_correct": False},
            ],
        },
    ]
    Orm.Quiz.create_quiz(
        "Geography of Ukraine Quiz", "A quiz with questions about the geography of Ukraine", geography_ukraine_questions
    )
