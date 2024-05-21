import os

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage

load_dotenv()

TG_BOT_API_TOKEN = os.getenv("TG_BOT_API_TOKEN")

bot = AsyncTeleBot(TG_BOT_API_TOKEN, state_storage=StateMemoryStorage())
