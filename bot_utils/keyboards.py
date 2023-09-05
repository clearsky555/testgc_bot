from aiogram import types


def get_menu_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    info = types.InlineKeyboardButton('Информация', callback_data='info')
    register = types.InlineKeyboardButton('Регистрация', callback_data='register')
    markup.add(info, register)
    return markup