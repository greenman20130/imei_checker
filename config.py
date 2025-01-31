import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Конфигурация
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_TOKEN = os.getenv('API_TOKEN')
AUTHENTICATION_TOKEN = os.getenv('AUTHENTICATION_TOKEN')
WHITELIST_USERS = ['user1_id', 'user2_id']