from app import create_app
from bot.telegram_bot import start_bot
import threading
import asyncio

app = create_app()

def run_webapp():
    """Запуск Flask приложения"""
    app.run(debug=True, use_reloader=False, port=5000)

async def main():
    """Основная функция для запуска приложения"""
    # Запускаем Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_webapp, daemon=True)
    flask_thread.start()
    
    # Запускаем бота
    try:
        await start_bot()
    except KeyboardInterrupt:
        print("\nBot stopped")
    except Exception as e:
        print(f"Bot error: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Application error: {e}") 