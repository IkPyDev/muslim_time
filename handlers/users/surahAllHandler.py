from aiogram import types

from keyboards.inline.locationInline import location_callback

# from keyboards.inline.surahInline import surah_callback

from keyboards.default.menuKeyboards import menuStart
from parsings.surahAll import surah_all
from keyboards.inline.surahInlineAll import *
from loader import dp, bot
from keyboards.inline.surahInlineAll import kirish_surah,ikkichi_surah,surah_callback4,surah_callback5,surah_callback6


@dp.callback_query_handler(kirish_surah.filter(item_name="1811"))
async def surah_keyingisi(call: types.CallbackQuery):
    await call.message.edit_reply_markup(surahsMenu2)

@dp.callback_query_handler(kirish_surah.filter(item_name="1"))
async def surah_Key1(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда \nБир оз кутинг Илтимос")
    surah = surah_all(1)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>\nБошланди\n👇👇👇\n{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)
@dp.callback_query_handler(kirish_surah.filter(item_name="1"))
async def surah_Key1(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда \nБир оз кутинг Илтимос")
    surah = surah_all(1)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>\n👇👇👇\n{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)


@dp.callback_query_handler(kirish_surah.filter(item_name="2"))
async def surah_Key2(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(2)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>\n👇👇👇\n{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="3"))
async def surah_Key3(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(3)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>\n👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="4"))
async def surah_Key4(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(4)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="5"))
async def surah_Key5(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(5)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="6"))
async def surah_Key6(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(6)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="7"))
async def surah_Key7(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(7)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="8"))
async def surah_Key8(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(8)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="9"))
async def surah_Key9(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(9)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="10"))
async def surah_Key10(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(10)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="11"))
async def surah_Key11(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(11)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="12"))
async def surah_Key12(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(12)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="13"))
async def surah_Key13(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(13)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="14"))
async def surah_Key14(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(14)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="15"))
async def surah_Key15(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(15)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="16"))
async def surah_Key16(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(16)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="17"))
async def surah_Key17(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(17)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="18"))
async def surah_Key18(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(18)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)

@dp.callback_query_handler(kirish_surah.filter(item_name="19"))
async def surah_Key19(call: types.CallbackQuery):
    await call.message.answer("Малумотлар юкланмоқда Бир оз кутинг Илтимос")
    surah = surah_all(19)
    titel = surah["title"]
    text = surah["text"]
    audio = surah["audio"]
    msg = f"<b> {titel} </b>👇👇👇{text}"
    await call.message.delete()
    await call.message.answer_audio(audio)
    await call.message.answer(msg)


@dp.callback_query_handler(ikkichi_surah.filter(item_name="1811"))
async def surah_keyingisi1(call: types.CallbackQuery):
    await call.message.edit_reply_markup(surahsMenu3)

@dp.callback_query_handler(ikkichi_surah.filter(item_name="1812"))
async def surrah_ikkinchisi12(call: types.CallbackQuery):
    await call.message.edit_reply_markup(surahsMenu1)

