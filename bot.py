import telebot
from config import TELEGRAM_BOT_TOKEN, WHITELIST_USERS
from imei_service import ImeiService

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: message.from_user.id in WHITELIST_USERS)
def handle_imei(message):
    imei = message.text
    result = ImeiService.check_imei(imei)
    bot.reply_to(message, f"Информация о IMEI: {result}")

# Запуск бота
if __name__ == '__main__':
    bot.polling()