import logging

from aiogram import Dispatcher, types

from config import ADMINS, WEBHOOK_URL


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(
                admin,
                'Hello, Creators!\nI was successfully launched!'
            )

        except Exception as err:
            logging.exception(err)


async def set_default_commands(dp, bot):
    await bot.set_webhook(WEBHOOK_URL)
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
            types.BotCommand("help", "help"),
        ]
    )


async def is_in_private_chat(message: types.Message):
    return message.from_user.id == message.chat.id
