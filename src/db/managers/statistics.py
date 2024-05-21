from sqlalchemy.orm import Session

from db.models import Statistics


class StatisticsManager:
    def __init__(self, session: Session):
        self.session = session

    def get_user_statistics(self, user_id):
        return self.session.query(Statistics).filter_by(user_id=user_id).all()

    def get_statistics_by_id(self, statistics_id):
        return self.session.query(Statistics).filter_by(id=statistics_id).first()
    
    def get_statistics_by_quiz_id_user_id(self, quiz_id, user_id):
        return self.session.query(Statistics).filter_by(quiz_id=quiz_id, user_id=user_id).first()
