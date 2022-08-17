import logging

from aiogram import types

from keyboards.inline.locationInline import location_callback

from keyboards.default.menuKeyboards import menuStart

from loader import dp, bot, db
from utils.db_api.data import Database
# db = Database()

#🌏Mинтака Inline keyboard
# @dp.callback_query_handler(location_callback.filter(item_name="5"))
# async def get_location(call: types.CallbackQuery):
#     idd = int(call.from_user.id)
#     region = "5"
#     db.update_user_region(region,idd)
#     await call.answer("Сизни миткангиз Guliston  деб танланди!", cache_time=60, show_alert=True)
#     await call.message.delete()
#     await call.message.answer("Бош менюдасиз",reply_markup=menuStart)
#
#
# @dp.callback_query_handler(location_callback.filter(item_name="27"))
# async def get_location(call: types.CallbackQuery):
#     # idd = int(call.from_user.id)
#     # f = call.from_user.id
#     # reg = "27"
#     # logging.info(idd)
#     # db.update_user_region(reg, idd)
#     # callback_data = call.data
#     # logging.info(f'{callback_data=}')
#     # logging.info(f'{call.from_user.id=}')
#     idd = int(call.from_user.id)
#     region = "27"
#     db.update_user_region(region, idd)
#     await call.answer('Сизни миткангиз Toshkent  деб танланди!', cache_time=60, show_alert=True)
#     await call.message.delete()
#     await call.message.answer("Bosh menyudasiz",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="43"))
async def get_location43(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "43"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ангрен деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="1"))
async def get_location1(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "1"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Андижон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="52"))
async def get_location52(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "52"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Арнасой деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="90"))
async def get_location90(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "90"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ашхабод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="2"))
async def get_location2(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "2"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Бекобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="3"))
async def get_location3(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "3"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Бишкек деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="76"))
async def get_location76(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "76"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Бойсун деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="73"))
async def get_location73(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "73"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Булоқбоши деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="44"))
async def get_location44(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "44"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Бурчмулла деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="4"))
async def get_location4(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "4"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Бухоро деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="46"))
async def get_location46(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "46"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Газли деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="5"))
async def get_location5(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "5"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Гулистон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="6"))
async def get_location6(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "6"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Денов деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="84"))
async def get_location84(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "84"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Деҳқонобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="51"))
async def get_location51(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "51"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Дўстлик деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="89"))
async def get_location89(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "89"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Душанбе деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="7"))
async def get_location7(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "7"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Жалолобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="8"))
async def get_location8(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "8"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Жамбул деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="9"))
async def get_location9(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "9"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Жиззах деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="10"))
async def get_location10(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "10"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Жомбой деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="61"))
async def get_location61(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "61"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Зарафшон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="50"))
async def get_location50(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "50"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Зомин деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="11"))
async def get_location11(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "11"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Каттақўрғон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="12"))
async def get_location12(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "12"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Конибодом деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="59"))
async def get_location59(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "59"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Конимех деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="86"))
async def get_location86(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "86"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Косон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="34"))
async def get_location34(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "34"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Косонсой деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="13"))
async def get_location13(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "13"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Марғилон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="64"))
async def get_location64(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "64"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Мингбулоқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="88"))
async def get_location88(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "88"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Муборак деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="68"))
async def get_location68(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "68"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Мўйноқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="14"))
async def get_location14(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "14"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Навоий деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="15"))
async def get_location15(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "15"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Наманган деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="16"))
async def get_location16(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "16"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Нукус деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="17"))
async def get_location17(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "17"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Нурота деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="41"))
async def get_location41(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "41"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Олмаота деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="45"))
async def get_location45(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "45"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Олот деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="38"))
async def get_location38(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "38"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Олтиариқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="69"))
async def get_location69(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "69"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Олтинкўл деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="49"))
async def get_location49(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "49"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Пахтаобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="32"))
async def get_location32(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "32"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Поп деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="39"))
async def get_location39(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "39"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Риштон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="42"))
async def get_location42(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "42"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Сайрам деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="18"))
async def get_location18(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "18"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Самарқанд деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="87"))
async def get_location87(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "87"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Таллимаржон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="66"))
async def get_location66(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "66"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Тахтакўпир деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="74"))
async def get_location74(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "74"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Термиз деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="58"))
async def get_location58(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "58"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Томди деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="27"))
async def get_location27(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "27"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Тошкент деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="92"))
async def get_location92(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "92"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Тошҳовуз деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="19"))
async def get_location19(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "19"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Туркистон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="91"))
async def get_location91(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "91"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Туркманобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="65"))
async def get_location65(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "65"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Тўрткўл деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="62"))
async def get_location62(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "62"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Узунқудуқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="78"))
async def get_location78(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "78"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Урганч деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="72"))
async def get_location72(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "72"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ургут деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="53"))
async def get_location53(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "53"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ўсмат деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="56"))
async def get_location56(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "56"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Учтепа деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="63"))
async def get_location63(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "63"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Учқудуқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="36"))
async def get_location36(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "36"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Учқўрғон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="20"))
async def get_location20(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "20"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ўш деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="57"))
async def get_location57(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "57"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ўғиз деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="37"))
async def get_location37(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "37"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Фарғона деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="79"))
async def get_location79(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "79"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хазорасп деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="21"))
async def get_location21(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "21"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хива деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="31"))
async def get_location31(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "31"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хонобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="80"))
async def get_location80(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "80"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хонқа деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="22"))
async def get_location22(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "22"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хўжанд деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="29"))
async def get_location29(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "29"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Хўжаобод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="67"))
async def get_location67(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "67"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Чимбой деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="23"))
async def get_location23(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "23"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Чимкент деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="35"))
async def get_location35(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "35"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Чортоқ деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="33"))
async def get_location33(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "33"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Чуст деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="28"))
async def get_location28(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "28"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Шаҳрихон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="77"))
async def get_location77(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "77"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Шеробод деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="82"))
async def get_location82(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "82"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Шовот деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="70"))
async def get_location70(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "70"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Шуманай деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="81"))
async def get_location81(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "81"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Янгибозор деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="55"))
async def get_location55(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "55"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ғаллаорол деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="85"))
async def get_location85(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "85"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Ғузор деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="93"))
async def get_location93(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "93"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қарши деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="60"))
async def get_location60(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "60"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қизилтепа деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="48"))
async def get_location48(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "48"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қоракўл деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="47"))
async def get_location47(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "47"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қоровулбозор деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="40"))
async def get_location40(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "40"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қува деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="75"))
async def get_location75(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "75"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қумқўрғон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="71"))
async def get_location71(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "71"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қўнғирот деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="30"))
async def get_location30(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "30"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қўрғонтепа деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)



@dp.callback_query_handler(location_callback.filter(item_name="26"))
async def get_location26(call: types.CallbackQuery):
    idd, region = int(call.from_user.id), "26"
    db.update_user_region(region,idd)
    await call.answer("Сизни Минтақагиз Қўқон деб танланди!", cache_time=60, show_alert=True)
    await call.message.delete()
    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)
