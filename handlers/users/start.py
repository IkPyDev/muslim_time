from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
from utils.allUsers import allUser
from keyboards.inline.locationInline import locationMenu
import asyncio
from aiogram.dispatcher import FSMContext
try:
    db.create_table_users()
except:
    pass

@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message,state: FSMContext):
    # logging.info(message)
    idd = int(message.from_user.id)
    name = message.from_user.full_name
    try:
        db.add_user(idd, name)
    except:
       pass
    # logging.info(idd)
    msg = f"{message.from_user.full_name}!\n"
    msg += "Ассалому алайкум ва роҳматуллоҳи ва барокатуҳ\n"
    msg += f"Мен Намоз ва Руза вактиларини айтувчи бот ман\n\n\n"
    adminga_xat = f'Starni bosdi:{message}'
    await message.answer(msg)
    await dp.bot.send_message(-1001777080199, adminga_xat)
    await message.answer("5 сонияда минтақалар пайдо болади\nИлтимос бот тогри ишлаши учун зарур минтақани танлаш❗️❗️❗️")
    allUser.add(message.from_user.id)
    await asyncio.sleep(5)
    await message.answer("Минтақангизни танланг", reply_markup=locationMenu)
    await state.finish()

