import logging
import asyncio

from aiogram import Bot, Dispatcher, types, executor

import config
from keyboards import mainMenu
from utils import on_startup_notify


BOT_TOKEN = config.BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, loop=asyncio.get_event_loop())

dp = Dispatcher(bot)

async def on_startup(dp):
    await on_startup_notify(dp, bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=f'Hi, {message.from_user.username}!',
        reply_markup=mainMenu
    )


@dp.message_handler(commands=['help', 'dev_info'])
async def send_help_message(message: types.Message):
    if message.text == '/help':
        await bot.send_message(
            message.from_user.id,
            text=(
                '/start - to start the bot\n'
                '/help - to get help for this bot\n'
                '/dev_info - about the developer\n'
            ),
            reply_markup=mainMenu
        )
    else:
        await bot.send_message(
            message.from_user.id,
            text=(
            'I do not know much about my developer. :(\n'
            'The only thing o know, that this is his github: https://github.com/Yakov-Varnaev'
            ),
            reply_markup=mainMenu
        )


@dp.message_handler()
async def handler(message: types.Message):
    text = message.text

    if '#собес_вопросы' in text:
        await message.pin()
        await bot.send_message(
            message.chat.id,
            text = 'Hey!\nI`ve pinned a message for you!'
        )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )
