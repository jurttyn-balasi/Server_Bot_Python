from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
main_menu=ReplyKeyboardMarkup(resize_keyboard=True)

menu=KeyboardButton(text='Menu')
main_menu.add(menu)
