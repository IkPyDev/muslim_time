from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Ботни ишга тушуриш ёки қайтадан бошлаш"),
            types.BotCommand("help", "Ёрдам"),
            types.BotCommand("users", "Обуначилар сони"),
        ]
    )
