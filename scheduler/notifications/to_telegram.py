import telegram
from scheduler.scheduler.settings import BOT_TOKEN


def send_telegram_message(telegram_id, message) -> None:
    bot_token = BOT_TOKEN
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=telegram_id, text=message)
