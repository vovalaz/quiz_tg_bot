import telebot

from db.orm import Orm
from telegram import markups
from telegram.bot import bot
from telegram.states import QuizStates


@bot.message_handler(commands=["start", "restart", "help"])
async def start_message(message: telebot.types.Message):
    await bot.set_state(message.from_user.id, QuizStates.choosing_quiz, message.chat.id)
    Orm.UserInfo.create_user_if_not_exists(message.from_user.username, message.from_user.id)
    quizzes = Orm.Quiz.get_all_quizzes()
    await bot.reply_to(
        message, "Hi, I'm quiz bot. \nSelect quiz you want to take", reply_markup=markups.quizzes_list_markup(quizzes)
    )


@bot.message_handler(state=QuizStates.choosing_quiz)
async def selecting_quiz(message: telebot.types.Message):
    quiz = Orm.Quiz.get_quiz_by_title(message.text)
    Orm.Message.create_message(message.from_user.id, message.text, message.chat.id, from_bot=False)
    if quiz:
        await bot.set_state(message.from_user.id, QuizStates.accepting_quiz, message.chat.id)
        await bot.reply_to(
            message,
            f"You selected: {quiz.title}\n{quiz.description}\nDo you want to start?",
            reply_markup=markups.confirmation_markup(),
        )
    else:
        quizzes = Orm.Quiz.get_all_quizzes()
        await bot.reply_to(
            message, "Quiz not found. Please select a valid quiz.", reply_markup=markups.quizzes_list_markup(quizzes)
        )


@bot.message_handler(state=QuizStates.accepting_quiz)
async def accepting_quiz(message: telebot.types.Message):
    if message.text.lower().strip() == "yes":
        previous_message = Orm.Message.get_last_message(message.from_user.id)
        quiz = Orm.Quiz.get_quiz_by_title(previous_message.message_text)
        if quiz:
            user_id = message.from_user.id
            Orm.UserQuizProgress.initialize_user_quiz_progress(user_id, quiz.id)
            first_question = Orm.Question.get_next_question(Orm.UserQuizProgress.get_user_quiz_progress(user_id))
            Orm.UserQuizProgress.update_user_quiz_progress(user_id, first_question.id)
            await bot.set_state(user_id, QuizStates.ongoing_quiz, message.chat.id)
            await send_next_question(user_id, message.chat.id)
    else:
        quizzes = Orm.Quiz.get_all_quizzes()
        await bot.set_state(message.from_user.id, QuizStates.choosing_quiz, message.chat.id)
        await bot.reply_to(message, "Select quiz you want to take", reply_markup=markups.quizzes_list_markup(quizzes))


@bot.message_handler(state=QuizStates.ongoing_quiz)
async def ongoing_quiz(message: telebot.types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_quiz_progress = Orm.UserQuizProgress.get_user_quiz_progress(user_id)

    if user_quiz_progress:
        current_question_id = user_quiz_progress.current_question_id
        question = Orm.Question.get_question_by_id(current_question_id)

        answer_text = message.text
        selected_answer = Orm.Answer.get_answer_by_text(question.id, answer_text)
        if selected_answer:
            Orm.UserAnswer.save_user_answer(user_id, question.id, selected_answer.id)

            next_question = Orm.Question.get_next_question(user_quiz_progress)
            if next_question:
                Orm.UserQuizProgress.update_user_quiz_progress(user_id, next_question.id)
                await send_next_question(user_id, chat_id)
            else:
                await bot.set_state(user_id, QuizStates.results, chat_id)
                Orm.UserQuizProgress.complete_user_quiz(user_id)
                await bot.reply_to(
                    chat_id, "Quiz completed! Thank you for participating.", reply_markup=markups.result_markup()
                )
        else:
            await bot.reply_to(chat_id, "Invalid answer. Please try again.")
    else:
        await bot.reply_to(chat_id, "Error in quiz progress. Please restart the quiz.")


async def send_next_question(user_id, chat_id):
    user_quiz_progress = Orm.UserQuizProgress.get_user_quiz_progress(user_id)
    current_question_id = user_quiz_progress.current_question_id
    question = Orm.Question.get_question_by_id(current_question_id)
    answers = Orm.Answer.get_answers_by_question_id(question.id)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for answer in answers:
        markup.add(answer.answer_text)
    await bot.send_message(chat_id, question.question_text, reply_markup=markup)
