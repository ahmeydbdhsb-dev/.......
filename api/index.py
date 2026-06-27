from flask import Flask, request
import telebot

app = Flask(__name__)

BOT_TOKEN = '8668088040:AAE3DVD67ZitM04nBOtnW7GSiYzDc7u2rF8'
YOUR_IDS = [1778665778, 8353977153, 8506998640]

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """🌟 أهلاً بك في بوت شاومنج 2026 🚀

━━━━━━━━━━━━━━━━━━
⚠️ لا تشغل بالك بالامتحان.. نحن هنا لنتولى الأمر.

⏰ تنبيه: تصلك الأسئلة والحلول النموذجية هنا في البوت بعد بدء اللجنة بـ 30 دقيقة بالضبط.
🎯 كن مستعداً، فالسرعة والدقة هما عنواننا.
━━━━━━━━━━━━━━━━━━

🛡️ ثق في قدراتك، ونحن سنكون سندك في هذه المهمة.
🔥 بالتوفيق يا بطل، أنت لها!""")

@bot.channel_post_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.username == 'shawm7ng2026':
        for user_id in YOUR_IDS:
            bot.forward_message(user_id, message.chat.id, message.message_id)

@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_json())
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/set_webhook')
def set_webhook():
    bot.set_webhook(url='https://tau-ten-50.vercel.app/' + BOT_TOKEN)
    return 'Webhook set!'

@app.route('/')
def home():
    return 'البوت شغال'
