import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Telegram configuration
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    WEBAPP_URL = os.environ.get('WEBAPP_URL')
    
    # ID администратора в Telegram для получения заявок
    ADMIN_TELEGRAM_ID = os.environ.get('ADMIN_TELEGRAM_ID') 