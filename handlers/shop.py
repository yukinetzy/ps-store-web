from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
from config import DB_PATH

router = Router()

@router.message(F.text == '🛍️ Магазин')
async def show_shop(message: Message):
    region = "TR"
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()

    curs.execute('SELECT id, name, price FROM products WHERE region = ?', (region,))
    products = curs.fetchall()
    conn.close()

    if not products:
        await message.answer("Товары не найдены.")
        return

    for product in products:
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(callback_data=f"add_{product[0]}")]
        ])
        await message.answer(f"*{product[1]}*\nЦена: {product[2]}₽", parse_mode="Markdown", reply_markup=markup)


# Добавление товара в корзину
@router.callback_query(F.data.startswith('add_'))
async def add_to_cart(callback: CallbackQuery):
    product_id = int(callback.data.split('_')[1])
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    try:
        curs.execute('INSERT INTO cart (user_id, product_id) VALUES (?, ?)', (callback.from_user.id, product_id))
        conn.commit()
        await callback.answer("Товар добавлен в корзину!")
    except sqlite3.Error as e:
        await callback.answer(f"Ошибка: {e}")
    finally:
        conn.close()
