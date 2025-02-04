from flask import Blueprint, render_template, request, jsonify
from bot.telegram_bot import bot
from config import Config

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/submit-form', methods=['POST'])
async def submit_form():
    try:
        data = request.json
        
        # Формируем сообщение для отправки в Telegram
        message = (
            "📝 New Contact Form Submission\n\n"
            f"👤 Name: {data.get('name')}\n"
            f"📧 Email: {data.get('email')}\n"
            f"📱 Phone: {data.get('phone')}\n"
            f"💼 Service: {data.get('service')}\n"
            f"💬 Message:\n{data.get('message')}"
        )
        
        # Отправляем сообщение администратору (можно указать ID админа в конфиге)
        await bot.send_message(chat_id=Config.ADMIN_TELEGRAM_ID, text=message)
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500 