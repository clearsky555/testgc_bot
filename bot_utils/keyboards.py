from aiogram import types


def get_language_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    kyrgyz = types.InlineKeyboardButton('Кыргызча 🇰🇬', callback_data='kyrgyz')
    russian = types.InlineKeyboardButton('Русский 🇷🇺', callback_data='russian')
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


def get_gender_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    male = types.InlineKeyboardButton('мужской(male)', callback_data='male')
    female = types.InlineKeyboardButton('женский(female)', callback_data='female')
    markup.add(male, female)
    return markup


def get_eligibility_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    yes = types.InlineKeyboardButton('yes', callback_data='eligibility_yes')
    no = types.InlineKeyboardButton('country claiming eligibility', callback_data='claiming_eligibility')
    markup.add(yes, no)
    return markup


def get_family_status_button(language):
    markup = types.InlineKeyboardMarkup(row_width=1)
    if language == 'russian':
        single = types.InlineKeyboardButton('холост/не замужем', callback_data='unmarried')
        married = types.InlineKeyboardButton('женат/замужем', callback_data='married')
        divorced = types.InlineKeyboardButton('разведён/разведена', callback_data='divorced')
        widowed = types.InlineKeyboardButton('вдовец/вдова', callback_data='widowed')
        l_s = types.InlineKeyboardButton('legally separated', callback_data='legally separated')
    else:  # По умолчанию, используем кыргызский язык
        single = types.InlineKeyboardButton('бүйүксүз/кыз алган жок(холост)', callback_data='single')
        married = types.InlineKeyboardButton('жеңишке/жат алган(женат)', callback_data='married')
        divorced = types.InlineKeyboardButton('болушпаган/болушпаган жок(разведен)', callback_data='divorced')
        widowed = types.InlineKeyboardButton('артыкчы/артыкчы жок(вдовец)', callback_data='widowed')
        l_s = types.InlineKeyboardButton('legally separated', callback_data='legally separated')

    markup.add(single, married, divorced, widowed, l_s)
    return markup


def get_level_education_button():
    markup = types.InlineKeyboardMarkup(row_width=1)
    ps = types.InlineKeyboardButton('primary school only', callback_data='p_s_only')
    hs_no_d = types.InlineKeyboardButton('high school, no degree', callback_data='h_s_no_degree')
    hs = types.InlineKeyboardButton('high school degree', callback_data='h_s')
    vs = types.InlineKeyboardButton('vocational school', callback_data='v_s')
    some_u_courses = types.InlineKeyboardButton('some university courses', callback_data='some_u_courses')
    ud = types.InlineKeyboardButton('university degree', callback_data='u_d')
    some_graduate_l_courses = types.InlineKeyboardButton('some graduate level courses', callback_data='s_g_l_c')
    md = types.InlineKeyboardButton("master's degree", callback_data='m_d')
    some_d_level_courses = types.InlineKeyboardButton('some doctorate level courses', callback_data='s_d_l_c')
    dd = types.InlineKeyboardButton('doctorate degree', callback_data='d_d')
    markup.add(ps,hs_no_d,hs,vs,some_u_courses,ud,some_graduate_l_courses, md, some_d_level_courses,dd)
    return markup

