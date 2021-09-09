from aiogram import types

import config


async def is_admin(message: types.Message):
    return message.from_user.id in config.ADMINS
