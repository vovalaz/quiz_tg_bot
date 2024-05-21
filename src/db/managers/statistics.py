from sqlalchemy.orm import Session

from db.models import Statistics


class StatisticsManager:
    def __init__(self, session: Session):
        self.session = session
