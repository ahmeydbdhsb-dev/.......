from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import telebot
import asyncio
import threading

app = Flask(__name__)

SESSION_STRING = 'YOUR_SESSION'
API_ID = 30478732
API_HASH = '394d6d66d2097791253e89282b6f4318'
BOT_TOKEN = '8668088040:AAE3DVD67ZitM04nBOtnW7GSiYzDc7u2rF8'
YOUR_ID = 1778665778

bot = telebot.TeleBot(BOT_TOKEN)
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats='shawm7ng2026'))
async def handler(event):
    if event.message.photo:
        photo = await event.message.download_media(bytes)
        bot.send_photo(YOUR_ID, photo)

def run_client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client.start())
    loop.run_forever()

threading.Thread(target=run_client, daemon=True).start()

@app.route('/')
def home():
    return "البوت شغال"
