# from parsings.locationParsing import get_location
# from utils.db_api.data import Database
# #
# for i in range(7,39):
#     print(f'@dp.callback_query_handler(surah_callback.filter(item_name={i}))\n'
#           f'async def get_surah{i}(call: types.CallbackQuery):\n'
#           f'surah = get_surah_section()[{i}]\n')



#
#
# def test():
#     db = Database()
#     try:
#         db.create_table_users()
#
#         db.add_user(12547824,"ikpydev")
#         db.add_user(58744141,"ikrombek")
#     except Exception as err:
#         pass
#     db.update_user_region(58,12547824)
#
#     user = db.user_region(id=5489210212)
#     print(f"regionni {user}")
#
#     users = db.select_all_users()
#     print(users)
#
#
# test()

regions = get_location()

for key, value in regions.items():
    print(f'@dp.callback_query_handler(location_callback.filter(item_name="{value}"))\nasync def get_location{value}(call: types.CallbackQuery):\n    idd, region = int(call.from_user.id), "{value}"\n    db.update_user_region(region,idd)\n    await call.answer("Сизни миткангиз {key} деб танланди!", cache_time=60, show_alert=True)\n    await call.message.delete()\n    await call.message.answer("Бош менюдасиз",reply_markup=menuStart)\n\n\n')
