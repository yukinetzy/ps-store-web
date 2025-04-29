from aiogram import types, Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
import sqlite3
from config import DB_PATH

router = Router()

@router.message(F.text == '🛒 Корзина')
async def show_cart(message: Message):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute('''
        SELECT products.id, products.name, products.price 
        FROM cart JOIN products ON cart.product_id = products.id
        WHERE cart.user_id = ?
    ''', (message.from_user.id,))
    items = curs.fetchall()
    conn.close()

    if not items:
        await message.answer("Корзина пуста")
        return

    total = sum(item[2] for item in items)
    for item in items:
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton("❌ Удалить", callback_data=f"remove_{item[0]}")]
        ])
        await message.answer(f"{item[1]} - {item[2]}₽", reply_markup=markup)

    await message.answer(f"\nИтого: {total}₽")

@router.callback_query(F.data.startswith('remove_'))
async def remove_from_cart(callback: CallbackQuery):
    product_id = int(callback.data.split('_')[1])
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute('DELETE FROM cart WHERE user_id = ? AND product_id = ? LIMIT 1',
                 (callback.from_user.id, product_id))
    conn.commit()
    conn.close()
    await callback.answer("Удалено из корзины!")