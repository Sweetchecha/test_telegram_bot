import asyncio
from datetime import datetime, timedelta
from database import Session, User

async def send_scheduled_message(bot, chat_id, message, delay_seconds):
    await asyncio.sleep(delay_seconds)
    await bot.send_message(chat_id=chat_id, text=message)

def schedule_messages(app):
    loop = asyncio.get_event_loop()
    session = Session()
    users = session.query(User).all()
    session.close()

    for user in users:
        loop.create_task(send_scheduled_message(app.bot, user.telegram_id, "Запланированное сообщение", 60))
