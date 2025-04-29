import asyncio
from aiogram import Router
from config import bot, dp
from db.database import init_db
from handlers import start, shop, cart, profile

async def main():
    init_db()
    dp.include_routers(start.router, shop.router, cart.router, profile.router)
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())