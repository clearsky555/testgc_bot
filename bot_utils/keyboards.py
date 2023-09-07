from aiogram import types


def get_menu_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    info = types.InlineKeyboardButton('Информация', callback_data='info')
    register = types.InlineKeyboardButton('Регистрация', callback_data='register')
    markup.add(info, register)
    return markup


def get_family_status_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    single = types.InlineKeyboardButton('холост/не замужем', callback_data='single')
    married = types.InlineKeyboardButton('женат/замужем', callback_data='married')
    divorced = types.InlineKeyboardButton('разведён/разведена', callback_data='divorced')
    widowed = types.InlineKeyboardButton('вдовец/вдова', callback_data='widowed')

    markup.add(single, married, divorced, widowed)
    return markup
