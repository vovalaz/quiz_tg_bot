from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.user_id"))
    message_text = Column(Text)
    chat_id = Column(Integer)
    from_bot = Column(Boolean)


class UserInfo(Base):
    __tablename__ = "userinfo"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255))


class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.user_id"))
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    score = Column(Float)
    max_score = Column(Float)
    completion_time = Column(Float)
    completed_at = Column(DateTime)

    user = relationship("UserInfo")
    quiz = relationship("Quiz")


class Quiz(Base):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)

    questions = relationship("Question", back_populates="quiz")
    statistics = relationship("Statistics", back_populates="quiz")


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    question_text = Column(Text)

    quiz = relationship("Quiz", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("question.id"))
    answer_text = Column(Text)
    is_correct = Column(Boolean)

    question = relationship("Question", back_populates="answers")


class UserAnswer(Base):
    __tablename__ = "user_answer"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.user_id"))
    question_id = Column(Integer, ForeignKey("question.id"))
    answer_id = Column(Integer, ForeignKey("answer.id"))
    answered_at = Column(DateTime, default=datetime.now)

    user = relationship("UserInfo")
    question = relationship("Question")
    answer = relationship("Answer")


class UserQuizProgress(Base):
    __tablename__ = "user_quiz_progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.user_id"))
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    current_question_id = Column(Integer, ForeignKey("question.id"))
    started_at = Column(DateTime, default=datetime.now)

    user = relationship("UserInfo")
    quiz = relationship("Quiz")
    current_question = relationship("Question")
