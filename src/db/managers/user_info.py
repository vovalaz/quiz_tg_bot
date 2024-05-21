from sqlalchemy.orm import Session

from db.models import UserInfo


class UserInfoManager:
    def __init__(self, session: Session):
        self.session = session

    def create_user_if_not_exists(self, username, user_id):
        user = self.session.query(UserInfo).filter_by(username=username, user_id=user_id).first()
        if user is None:
            new_user = UserInfo(username=username, user_id=user_id)
            self.session.add(new_user)
            self.session.commit()
            return new_user
        return user
