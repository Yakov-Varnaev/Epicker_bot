from aiogram import Dispatcher


from bot.app import dp
from .throttling import ThrottlingMiddleware

if __name__ == 'middlewares':
    dp.middleware.setup(ThrottlingMiddleware())