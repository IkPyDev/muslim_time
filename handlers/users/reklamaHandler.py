import asyncio



from aiogram.types import Message, ContentTypes
from aiogram import dispatcher

from utils.allUsers import allUser
from utils.db_api.data import Database
from loader import dp, db, bot

from aiogram.dispatcher import FSMContext
from data.config import ADMINS
@dp.message_handler(commands="users")
async def user_all(msg: Message):
    await dp.bot.send_message(chat_id=msg.from_user.id,text=f"Ройхатдан отган обуначилар:{len(db.select_all_users())}")


@dp.message_handler(text="/reklama",user_id=ADMINS)
async def rek_ad(msg:Message,state:FSMContext):
    users = db.select_all_users()

    await msg.answer(f"{len(users)} obunachiga xabar yuboring ")
    await state.set_state("Reklama")

@dp.message_handler(state="Reklama",content_types=ContentTypes.ANY)
async def rek_addd(msg: ContentTypes.ANY, state: FSMContext):
    users = db.select_all_users()
    s, b = 1, 1
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=msg.from_user.id, message_id=msg.message_id, protect_content=True)
            await asyncio.sleep(0.05)
            s += 1
        except Exception:
            b += 1
            pass

    await msg.answer(f"reklama {s} odmaga yuborildi, {b} odam blokladgan botni")
    await state.finish()

