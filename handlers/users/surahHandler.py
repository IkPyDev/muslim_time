from aiogram import types

from keyboards.inline.locationInline import location_callback

from keyboards.inline.surahInline import surah_callback

from keyboards.default.menuKeyboards import menuStart
from parsings.surahParsing import get_surah_section

from loader import dp, bot


#🌏Mинтака Inline keyboard
@dp.callback_query_handler(surah_callback.filter(item_name="1"))
async def get_surah1(call: types.CallbackQuery):
    surah = get_surah_section()[1]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)

@dp.callback_query_handler(surah_callback.filter(item_name="2"))
async def get_surah2(call: types.CallbackQuery):
    surah = get_surah_section()[2]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)

@dp.callback_query_handler(surah_callback.filter(item_name="3"))
async def get_surah3(call: types.CallbackQuery):
    surah = get_surah_section()[3]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)

@dp.callback_query_handler(surah_callback.filter(item_name="4"))
async def get_surah4(call: types.CallbackQuery):
    surah = get_surah_section()[4]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"

    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)

@dp.callback_query_handler(surah_callback.filter(item_name="5"))
async def get_surah5(call: types.CallbackQuery):
    surah = get_surah_section()[5]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)

    # await call.message.answer_voice(mp3)
    # await call.answer("ishladi",show_alert=True,cache_time=60)

@dp.callback_query_handler(surah_callback.filter(item_name="6"))
async def get_surah(call: types.CallbackQuery):
    surah = get_surah_section()[6]
    # surah = surah["5"]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3,caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="7"))
async def get_surah7(call: types.CallbackQuery):
    surah = get_surah_section()[7]
    titel = surah["title"]
    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="8"))
async def get_surah8(call: types.CallbackQuery):
    surah = get_surah_section()[8]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="9"))
async def get_surah9(call: types.CallbackQuery):
    surah = get_surah_section()[9]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="10"))
async def get_surah10(call: types.CallbackQuery):
    surah = get_surah_section()[10]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="11"))
async def get_surah11(call: types.CallbackQuery):
    surah = get_surah_section()[11]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="12"))
async def get_surah12(call: types.CallbackQuery):
    surah = get_surah_section()[12]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="13"))
async def get_surah13(call: types.CallbackQuery):
    surah = get_surah_section()[13]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="14"))
async def get_surah14(call: types.CallbackQuery):
    surah = get_surah_section()[14]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="15"))
async def get_surah15(call: types.CallbackQuery):
    surah = get_surah_section()[15]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="16"))
async def get_surah16(call: types.CallbackQuery):
    surah = get_surah_section()[16]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="17"))
async def get_surah17(call: types.CallbackQuery):
    surah = get_surah_section()[17]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="18"))
async def get_surah18(call: types.CallbackQuery):
    surah = get_surah_section()[18]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="19"))
async def get_surah19(call: types.CallbackQuery):
    surah = get_surah_section()[19]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="20"))
async def get_surah20(call: types.CallbackQuery):
    surah = get_surah_section()[20]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="21"))
async def get_surah21(call: types.CallbackQuery):
    surah = get_surah_section()[21]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="22"))
async def get_surah22(call: types.CallbackQuery):
    surah = get_surah_section()[22]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="23"))
async def get_surah23(call: types.CallbackQuery):
    surah = get_surah_section()[23]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="24"))
async def get_surah24(call: types.CallbackQuery):
    surah = get_surah_section()[24]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="25"))
async def get_surah25(call: types.CallbackQuery):
    surah = get_surah_section()[25]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="26"))
async def get_surah26(call: types.CallbackQuery):
    surah = get_surah_section()[26]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="27"))
async def get_surah27(call: types.CallbackQuery):
    surah = get_surah_section()[27]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="28"))
async def get_surah28(call: types.CallbackQuery):
    surah = get_surah_section()[28]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="29"))
async def get_surah29(call: types.CallbackQuery):
    surah = get_surah_section()[29]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="30"))
async def get_surah30(call: types.CallbackQuery):
    surah = get_surah_section()[30]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="31"))
async def get_surah31(call: types.CallbackQuery):
    surah = get_surah_section()[31]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="32"))
async def get_surah32(call: types.CallbackQuery):
    surah = get_surah_section()[32]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="33"))
async def get_surah33(call: types.CallbackQuery):
    surah = get_surah_section()[33]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="34"))
async def get_surah34(call: types.CallbackQuery):
    surah = get_surah_section()[34]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="35"))
async def get_surah35(call: types.CallbackQuery):
    surah = get_surah_section()[35]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="36"))
async def get_surah36(call: types.CallbackQuery):
    surah = get_surah_section()[36]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="37"))
async def get_surah37(call: types.CallbackQuery):
    surah = get_surah_section()[37]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)


@dp.callback_query_handler(surah_callback.filter(item_name="38"))
async def get_surah38(call: types.CallbackQuery):
    surah = get_surah_section()[38]
    titel = surah["title"]


    text = surah["text"]
    mp3 = surah["audio"]
    arabic = surah["arabic"]
    msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
          f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
          f"{text}"
    await call.answer(titel, cache_time=60, show_alert=False)
    await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
    await call.message.answer(msg)
# for i in range(7,39):
#     @dp.callback_query_handler(surah_callback.filter(item_name=f'{i}'))
#     async def get_surah(call: types.CallbackQuery):
#         surah = get_surah_section()[i]
#         # surah = surah["5"]
#         titel = surah["title"]
#         text = surah["text"]
#         mp3 = surah["audio"]
#         arabic = surah["arabic"]
#         msg = f"Суранинг номи:<b>{titel}</b>\n\n\n" \
#               f"Араб тилида ёзилиши\n<b>{arabic}</b>\n\n\n" \
#               f"{text}"
#         await call.answer(titel, cache_time=60, show_alert=False)
#         await call.message.answer_voice(mp3, caption=f'{titel}\n👇👇👇')
#         await call.message.answer(msg)