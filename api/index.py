from flask import Flask, request
import telebot

app = Flask(__name__)

BOT_TOKEN = '8668088040:AAE3DVD67ZitM04nBOtnW7GSiYzDc7u2rF8'
YOUR_IDS = [1778665778, 8353977153]

bot = telebot.TeleBot(BOT_TOKEN)

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
