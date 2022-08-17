from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.surahInline import surahsMenu
from keyboards.inline.surahInlineAll import surahsMenu1
import logging

@dp.callback_query_handler(text="surahtoplam")
async def surah_toplam_kirish(call:CallbackQuery):
    await call.answer("Танланди", cache_time=60, show_alert=False)
    await call.message.edit_reply_markup(surahsMenu)


@dp.callback_query_handler(text="surahAll")
async def surah_all_kirish(call:CallbackQuery):
    await call.answer("Танланди",cache_time=60,show_alert=False)
    await call.message.edit_reply_markup(surahsMenu1)