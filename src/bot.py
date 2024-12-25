from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, Application
from handlers import handle_start, handle_message
from scheduler import schedule_messages
from database import initialize_database

from config import TOKEN

def main():
    # Инициализация базы данных
    initialize_database()

    # Создание приложения Telegram бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд и сообщений
    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск планировщика
    schedule_messages(app)

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()
