from aiogram import types


def get_language_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    kyrgyz = types.InlineKeyboardButton('Кыргызча', callback_data='kyrgyz')
    russian = types.InlineKeyboardButton('Русский', callback_data='russian')
    markup.add(kyrgyz, russian)
    return markup


# def get_menu_button():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     info = types.InlineKeyboardButton('Информация', callback_data='info')
#     register = types.InlineKeyboardButton('Регистрация', callback_data='register')
#     cancel = types.InlineKeyboardButton('отмена', callback_data='cancel')
#     markup.add(info, register, cancel)
#     return markup

def get_menu_button(language):
    markup = types.InlineKeyboardMarkup(row_width=1)

    if language == 'russian':
        info = types.InlineKeyboardButton('Информация', callback_data='info')
        register = types.InlineKeyboardButton('Регистрация', callback_data='register')
        cancel = types.InlineKeyboardButton('Отмена', callback_data='cancel')
    else:
        info = types.InlineKeyboardButton('Маалымат(информация)', callback_data='info')
        register = types.InlineKeyboardButton('Каттоо(регистрация)', callback_data='register')
        cancel = types.InlineKeyboardButton('Жокко чыгаруу(отмена)', callback_data='cancel')

    markup.add(info, register, cancel)
    return markup


def get_family_status_button(language):
    markup = types.InlineKeyboardMarkup(row_width=1)
    if language == 'russian':
        single = types.InlineKeyboardButton('холост/не замужем', callback_data='single')
        married = types.InlineKeyboardButton('женат/замужем', callback_data='married')
        divorced = types.InlineKeyboardButton('разведён/разведена', callback_data='divorced')
        widowed = types.InlineKeyboardButton('вдовец/вдова', callback_data='widowed')
    else:  # По умолчанию, используем кыргызский язык
        single = types.InlineKeyboardButton('бүйүксүз/кыз алган жок(холост)', callback_data='single')
        married = types.InlineKeyboardButton('жеңишке/жат алган(женат)', callback_data='married')
        divorced = types.InlineKeyboardButton('болушпаган/болушпаган жок(разведен)', callback_data='divorced')
        widowed = types.InlineKeyboardButton('артыкчы/артыкчы жок(вдовец)', callback_data='widowed')

    markup.add(single, married, divorced, widowed)
    return markup
