from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()

# Определение моделей
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(100))
    username = Column(String(100))

class MessageLog(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    message_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Настройка подключения к базе данных
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    Base.metadata.create_all(engine)

def save_user(telegram_id, first_name, username):
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id, first_name=first_name, username=username)
        session.add(user)
        session.commit()
    session.close()

def log_message(user_id, message_text):
    session = Session()
    log = MessageLog(user_id=user_id, message_text=message_text)
    session.add(log)
    session.commit()
    session.close()
