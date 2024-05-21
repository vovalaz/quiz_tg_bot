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
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("show results", "/restart")
    return keyboard


def back_to_results_markup():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add("Back to Results")
    return markup
