FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    BOT_TOKEN="7929733389:AAHLVW4QeyZ-Hnd7mNAtTRTbwf3lFsclDzk" \
    DATABASE_URL="postgresql://postgres:password@db:5432/telegram_bot"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/bot.py"]
