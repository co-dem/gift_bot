from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from conf import TOKEN, check_btn, show_users

import asyncio

user_num = 0
users_to_notify = {} # ids
users = {} # user_name: user_num
bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def notify():
    print('entered to notify')
    while True:
        await asyncio.sleep(15)
        for x, y in users_to_notify.items():
            await bot.send_message(y, '''Для того чтобы принять участие в розыгрыше, подпишитесь на всех спонсоров ниже и нажмите на кнопку:
✅ ПРОВЕРИТЬ

Спонсоры:
<a href="https://t.me/nightmane420">🥷 420</a>
<a href="https://t.me/klubnikanyashka00">🎀 klubnikanyashka</a>
    ''', parse_mode = 'HTML')


@dp.message_handler(content_types = 'text')
async def main(message: types.Message):
    if message.text.lower() == '/start' and message.from_id != 1809889367:
        with open('intro.mp4', 'rb') as vid:
            await bot.send_video(message.from_id, video = vid, caption = '''🎁 Розыгрыш от @NIGHTMANE420

💎 Вся инфа о конкурсе на канале

📲 по всем вопросам обращаться @trapx300''')
        if message.from_user.username not in users_to_notify:
            users_to_notify[message.from_user.username] = message.from_user.id
            print(users_to_notify)
        await bot.send_message(message.from_id, '''Для того чтобы принять участие в розыгрыше, подпишитесь на всех спонсоров ниже и нажмите на кнопку:
✅ ПРОВЕРИТЬ

Спонсоры:
<a href="https://t.me/nightmane420">🥷 420</a>
<a href="https://t.me/klubnikanyashka00">🎀 klubnikanyashka</a>
    ''', parse_mode = 'html', reply_markup = check_btn)
    
    if message.from_id == 1809889367 and message.text.lower() == '/start':
        await bot.send_message(1809889367, 'main text: passed', reply_markup = show_users)
    if message.from_id == 1809889367 and message.text.lower() == 'показать пользывателей':
        result = ''
        for x, y in users.items():
            result += f'@{x}\n {y}'
        if len(result) >= 3:
            await bot.send_message(1809889367, result)
        else:
            await bot.send_message(1809889367, 'user list is empty')

    await notify()
@dp.callback_query_handler(Text('checksub'))
async def cehck_sub_func(call: types.CallbackQuery):
    global users_to_notify, user_num, users
    askto = {'🥷 420': [-1001524457333, 'https://t.me/nightmane420'], '🎀 klubnikanyashka': [-1001700673722, 'https://t.me/klubnikanyashka00'], }
    users_to_notify[call.from_user.username] = call.from_user.id
    for x, y in askto.items():
        dt = await bot.get_chat_member(chat_id = y[0], user_id = call.from_user.id)
        print(dt)
        if call.data == 'checksub':
            if dt.status in ['creator', 'owner', 'administrator', 'member']:
                try:
                    del users_to_notify[call.from_user.username]
                    user_num += 1
                    await bot.send_message(call.from_user.id, f'''✅ Вы участник розыгрыша!

Ваш номер 🔜 {user_num}

За итогами следите на канале 💸

Спонсоры:
🥷 420 (https://t.me/nightmane420)
🎀 klubnikanyashka (https://t.me/klubnikanyashka00)''')
                    users[call.from_user.username] = user_num
                except (ValueError, KeyError):
                    users_to_notify[call.from_user.username] = call.from_user.id
                    users_to_notify.pop(call.from_user.username)
                    print(users_to_notify)
            else:
                await bot.send_message(call.from_user.id, f'подпишитесь на <a href="{y[1]}">{x}</a> и пройдите проверку заново', parse_mode = 'html')


executor.start_polling(dp)