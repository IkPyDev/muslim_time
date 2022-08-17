from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandHelp(),state="*")
async def bot_help(message: types.Message, state: FSMContext):
    text = ("Бу бот ҳали янги лекин Янгиланиб боради \nагар бот хато болса 10 сония яки 20 сониядан кейин қатадан жонатинг болмасa /start Буругуни қатадан юборинг \nАгар қандайдир хатони корсагиз @IkPyDev Жамосига юборинг")
    
    await message.answer(text)
    await state.finish()
