from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6027312689:AAGw3QhcjXdmmiqUrXg3Tq8YaI2JawxVtVU'

check_btn = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = '✅ Проверить', callback_data = 'checksub')]
    ]
)
dev_menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton('вкл')]
    ],
    resize_keyboard = True
)

show_users = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton('показать пользывателей')]
    ],
    resize_keyboard = True
)