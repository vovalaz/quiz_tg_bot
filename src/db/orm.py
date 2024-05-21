from sqlalchemy.orm import Session, sessionmaker

from db.database import engine
from db.managers import (AnswerManager, MessageManager, QuestionManager,
                         QuizManager, StatisticsManager, UserAnswerManager,
                         UserInfoManager, UserQuizProgressManager)

DBSession = sessionmaker(bind=engine)


class Orm:
    session: Session = DBSession()

    Answer = AnswerManager(session)
    Message = MessageManager(session)
    Question = QuestionManager(session)
    Quiz = QuizManager(session)
    Statistics = StatisticsManager(session)
    UserAnswer = UserAnswerManager(session)
    UserInfo = UserInfoManager(session)
    UserQuizProgress = UserQuizProgressManager(session)
