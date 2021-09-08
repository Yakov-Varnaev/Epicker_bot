from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



help_btn = KeyboardButton(text='/help')
dev_about_btn = KeyboardButton(text='about dev')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(help_btn).row(dev_about_btn)
