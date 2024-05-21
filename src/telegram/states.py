from telebot.asyncio_handler_backends import State, StatesGroup


class QuizStates(StatesGroup):
    choosing_quiz = State()
    accepting_quiz = State()
    ongoing_quiz = State()
    results = State()
