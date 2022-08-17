import logging
from aiogram import types

from data.config import ADMINS, CHENELS
from keyboards.inline.locationInline import locationMenu
from keyboards.inline.ramadanInline import ramadanMenu
from keyboards.default.namazKeyboards import namazButtons
from parsings.prayerTimes import get_prayer_times_for_today, get_prayer_times_for_tomorrow
import logging
from loader import dp, db
from utils.db_api.data import Database
@dp.message_handler(text='⏳📅Бугун')
async def get_today_prayer_time(message: types.Message):
    idd = message.from_user.id
    idd = int(idd)
    region = db.user_region(id=idd)
    try:
        today = get_prayer_times_for_today(f'{region[2]}')
        await message.answer(f'Бугун :\n{today} ', parse_mode="Markdown")
    except Exception as err:

        text = f'{err} kuzatildi manashu foydalanuvchida {message}'
        await dp.bot.send_message(CHENELS,text)
        await message.answer("❌Сиз ҳақизда малумот топилмади илтомос /start Буйруғни қайтадан юборинг❌")


@dp.message_handler(text='📆Eрта')
async def get_tommorow_prayer_time(message: types.Message):
    # await message.answer("⏳")
    # logging.info(message)
    idd = message.from_user.id
    idd = int(idd)
    region = db.user_region(id=idd)
    try:
        tommorow = get_prayer_times_for_tomorrow(region[2])
        await message.answer(f'Ертага :\n{tommorow} ', parse_mode="Markdown")
    except Exception as err:
        text = f'{err} kuzatildi manashu foydalanuvchida {message}'
        await dp.bot.send_message(CHENELS, text)
        await message.answer("❌Сиз ҳақизда малумот топилмади илтомос /start Буйруғни қайтадан юборинг❌")

@dp.message_handler(text='🤲 Саҳарлик & Ифторлик')
async def get_ramadan(message: types.Message):
    # logging.info(message)
    await message.answer(f'Танглан: ', reply_markup=ramadanMenu)


@dp.message_handler(text='🌏Mинтака')
async def get_location_inline_keyboards(message: types.Message):
    # logging.info(message)
    await message.answer("Минтақангизни озгартиринг:", reply_markup=locationMenu)


@dp.message_handler(text='🙏Намоз хакида кушимча малумотлар')
async def get_ramadan(message: types.Message):
    # logging.info(message)
    await message.answer('Тангланг', reply_markup=namazButtons)
    
    # surah = get_surah_section()
    # for id, value in surah.items():
    #     await message.answer_audio(value["audio"], caption=f'<b>{value["title"]}</b>')
    #     await message.answer(value['text'])
    #     await asyncio.sleep(10)
    
    
    



if __name__ == '__main__':
    print(get_ramadan())
