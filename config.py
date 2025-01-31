import os
from dotenv import load_dotenv


load_dotenv()

# Конфигурация
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_TOKEN = os.getenv('API_TOKEN')
AUTHENTICATION_TOKEN = os.getenv('AUTHENTICATION_TOKEN')
WHITELIST_USERS = [00000000000]