import logging

from aiogram import Dispatcher, types

from config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(
                admin,
                'Hello, Creators!\nI was successfully launched!'
            )

        except Exception as err:
            logging.exception(err)


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
            types.BotCommand("help", "help"),
        ]
    )
