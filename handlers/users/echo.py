from aiogram import types

from loader import dp


# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id,text="❌Бундай Буйруқ ёки Команда мавжуд эмас ❌")
