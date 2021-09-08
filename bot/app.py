import logging

from aiogram import Bot, Dispatcher, executor, types

import config
from keyboards import mainMenu
from utils import on_startup_notify


BOT_TOKEN = config.BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)

async def on_startup(dp):
    await on_startup_notify(dp)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Hi, {message.from_user.username}!',
        reply_markup=mainMenu
    )


if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
