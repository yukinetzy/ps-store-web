from aiogram import types, Router, F
import sqlite3
from config import DB_PATH

router = Router()

@router.message(F.text == '👤 Личный кабинет')
async def profile(message: types.Message):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()

    curs.execute('SELECT * FROM orders WHERE user_id=?', (message.from_user.id,))
    orders = curs.fetchall()

    curs.execute('SELECT * FROM subscriptions WHERE user_id=?', (message.from_user.id,))
    subs = curs.fetchall()

    conn.close()

    response = "📦 Заказы:\n"
    response += "\n".join([str(o) for o in orders]) if orders else "Нет заказов"
    response += "\n\n📅 Подписки:\n"
    response += "\n".join([str(s) for s in subs]) if subs else "Нет подписок"

    await message.answer(response)
