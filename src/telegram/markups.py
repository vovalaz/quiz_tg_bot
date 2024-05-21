import telebot
from db.models import Quiz


def quizzes_list_markup(quizzes: list[Quiz]):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    for quiz in quizzes:
        keyboard.add(quiz.title)
    return keyboard


def confirmation_markup():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("yes", "no")
    return keyboard


def result_markup():
    home_keyboard = telebot.types.ReplyKeyboardMarkup()
    home_keyboard.row("/опитування")
    return home_keyboard


def rec_markup():
    home_keyboard = telebot.types.ReplyKeyboardMarkup()
    home_keyboard.row("/рекомендація", "/опитування")
    return home_keyboard


def cancel_markup():
    cancel_keyboard = telebot.types.ReplyKeyboardMarkup()
    cancel_keyboard.row("/на_головну")
    return cancel_keyboard


def confirm_test_markup():
    cancel_keyboard = telebot.types.ReplyKeyboardMarkup()
    cancel_keyboard.row("/почати_опитування")
    return cancel_keyboard


def rating_markup():
    rating_keyboard = telebot.types.ReplyKeyboardMarkup()
    rating_keyboard.row("/пропустити", "/не_рекомендувати", "/закінчити")
    rating_keyboard.row("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    return rating_keyboard


def rating_recommendation_markup():
    rating_keyboard = telebot.types.ReplyKeyboardMarkup()
    rating_keyboard.row("/не_рекомендувати", "/закінчити")
    rating_keyboard.row("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    return rating_keyboard
