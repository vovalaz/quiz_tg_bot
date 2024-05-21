from sqlalchemy.orm import Session

from db.models import Message


class MessageManager:
    def __init__(self, session: Session):
        self.session = session

    def create_message(self, user_id: int, message_text: str, chat_id: int, from_bot: bool):
        new_message = Message(
            user_id=user_id,
            message_text=message_text,
            chat_id=chat_id,
            from_bot=from_bot
        )
        self.session.add(new_message)
        self.session.commit()
        return new_message

    def get_pre_last_message(self, user_id: int):
        messages = self.session.query(Message).filter_by(user_id=user_id).order_by(Message.id.desc()).limit(2).all()
        return messages[1] if len(messages) > 1 else None

    def get_last_message(self, user_id: int):
        return self.session.query(Message).filter_by(user_id=user_id).order_by(Message.id.desc()).first()
