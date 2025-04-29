import sqlite3
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from config import DB_PATH

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    username = message.from_user.first_name
    user_id = message.from_user.id

    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()

    try:
        curs.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # пользователь уже есть, ничего не делаем

    conn.close()

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть магазин", web_app=WebAppInfo(url="https://yukinetzy.github.io/ps-store-web/"))],
        [InlineKeyboardButton(text="🛒 Корзина", callback_data="cart_menu")],
        [InlineKeyboardButton(text="👤 Личный кабинет", callback_data="profile_menu")]
    ])

    await message.answer(f'''Привет, {username}! Этот Telegram-бот представляет собой удобный мини-магазин цифровых товаров из турецкого и индийского PlayStation Store. Он позволяет пользователям:

🔹 Просматривать каталог товаров, включая игры и подписки  
🔹 Добавлять товары в корзину и управлять её содержимым  
🔹 Отслеживать свою активную подписку  

Выберите действие:''', reply_markup=markup)
