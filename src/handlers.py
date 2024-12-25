from telegram import Update
from telegram.ext import CallbackContext
from database import save_user, log_message

async def handle_start(update: Update, context: CallbackContext):
    user = update.effective_user
    # Сохранить пользователя в базу данных
    save_user(user.id, user.first_name, user.username)
    # Отправить сообщение асинхронно
    await context.bot.send_message(chat_id=user.id, text="Привет! Я ваш автоматизированный помощник.")

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    user_id = update.effective_user.id
    log_message(user_id, text)

    if "услуга" in text:
        response = "Мы предлагаем онлайн-услуги. Напишите, чем можем помочь."
    elif "цена" in text:
        response = "Прайс-лист доступен на нашем сайте."
    else:
        response = "Извините, я пока не могу обработать это сообщение."

    await update.message.reply_text(response)
