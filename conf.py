from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6219951021:AAEsy-jlC98-nLHZCQSqtZwiwX2BIAHxZbU'

check_btn = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = '✅ Проверить', callback_data = 'checksub')]
    ]
)

show_users = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton('показать пользывателей')]
    ],
    resize_keyboard = True
)