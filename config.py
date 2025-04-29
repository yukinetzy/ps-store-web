from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import asyncio

BOT_TOKEN = ('7888464873:AAFkDYLi6JwpmihMx77dKOTe7BpM2_INrTc')
DB_PATH = 'data/PS_Store.sql'

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
