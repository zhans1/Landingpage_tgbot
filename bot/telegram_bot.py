from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from config import Config
import logging

# Настраиваем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Создаем объекты бота и диспетчера
bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    try:
        # Создаем кнопку для WebApp
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[[
                types.InlineKeyboardButton(
                    text="Open WebApp",
                    web_app=WebAppInfo(url=Config.WEBAPP_URL)
                )
            ]]
        )
        
        await message.answer(
            "Welcome! Click the button below to open the WebApp.",
            reply_markup=keyboard
        )
        logger.info(f"Sent WebApp button to user {message.from_user.id}")
        
    except Exception as e:
        logger.error(f"Error in start command: {e}", exc_info=True)
        await message.answer("Sorry, something went wrong.")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    help_text = """
Available commands:
/start - Start the bot and get WebApp button
/help - Show this help message
    """
    await message.answer(help_text)

@dp.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    """Обработчик данных от WebApp"""
    try:
        data = message.web_app_data.data
        logger.info(f"Received WebApp data from user {message.from_user.id}: {data}")
        await message.answer(f"Received your data: {data}")
    except Exception as e:
        logger.error(f"Error processing WebApp data: {e}", exc_info=True)
        await message.answer("Error processing your data")

async def start_bot():
    """Функция для запуска бота"""
    try:
        logger.info("Starting bot...")
        # Удаляем старые обновления и запускаем бота
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot startup error: {e}", exc_info=True)
        raise 

async def stop_bot():
    """Корректное завершение работы бота"""
    try:
        logger.info("Stopping bot...")
        await bot.session.close()
        await dp.storage.close()
        logger.info("Bot stopped")
    except Exception as e:
        logger.error(f"Error stopping bot: {e}", exc_info=True) 