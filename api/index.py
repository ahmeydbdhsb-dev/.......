from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import telebot
import asyncio
import threading

app = Flask(__name__)

SESSION_STRING = '1BJWap1wBu8KqfQpED4iXPwfYf52Xmv802SJSyEJ8efpaBXWo9kgQUWubYIjKKk73osRAaDE2LLnwW0aUl4SYMXT-VpsFufvmD3CIkYTgfp3fOpg2exH90odqXLa_L0s-9-lFKge0c6JuVfP7J-ivYw0_fTu59c0Sf8PAzTKY6feuZEvaBVZOFB8nZnPPvZsInvLMBR04ySvPZH1YyxROwiluxoUtH1KkVysIv2BQhViT1Aj5CzumTD_nDBPMqyN7cES4sVNdi3nm_VMUSh9aO3hYDGd0Hnbg6glLTihTyLWBHDUsLCND162krrF9xJQ3H3x3_lQ8PWDbThhQP31L9MfVWT8Sr5Q='
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
