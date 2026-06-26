from flask import Flask
from telethon import TelegramClient, events
import telebot
import asyncio
import os

app = Flask(__name__)
BOT_TOKEN = '8668088040:AAE3DVD67ZitM04nBOtnW7GSiYzDc7u2rF8'
YOUR_ID = 1778665778
bot = telebot.TeleBot(BOT_TOKEN)

# استخدام ملف الجلسة الموجود في نفس المجلد
client = TelegramClient('my_session', 30478732, '394d6d66d2097791253e89282b6f4318')

@client.on(events.NewMessage(chats='shawm7ng2026'))
async def handler(event):
    if event.message.photo:
        path = await event.download_media()
        with open(path, 'rb') as photo:
            bot.send_photo(YOUR_ID, photo, caption="📸 صورة جديدة تم التقاطها!")

@app.route('/')
def home():
    return "البوت يعمل الآن 24/7"

if __name__ == "__main__":
    client.start()
    app.run(host='0.0.0.0', port=5000)
