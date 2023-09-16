from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import TOKEN
from bot_utils import handlers as hs
from state import UserAddState

from aiogram import types

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# router
# commands
# dp.register_message_handler(hs.welcome_message, commands=['start'])
dp.register_message_handler(hs.language_selection, commands=['start'])

dp.register_message_handler(hs.set_user_data, state=UserAddState.add_user)
dp.register_message_handler(hs.add_user_name, state=UserAddState.add_user_name)
dp.register_message_handler(hs.add_user_surname, state=UserAddState.add_user_surname)
dp.register_message_handler(hs.add_user_middle_name, state=UserAddState.add_user_middle_name)
dp.register_message_handler(hs.add_birth_date, state=UserAddState.add_birth_date)
dp.register_message_handler(hs.add_birth_city, state=UserAddState.add_birth_city)
dp.register_message_handler(hs.add_birth_country, state=UserAddState.add_birth_country)
dp.register_message_handler(hs.add_country, state=UserAddState.add_country)
dp.register_message_handler(hs.add_city, state=UserAddState.add_city)
dp.register_message_handler(hs.add_street, state=UserAddState.add_street)
dp.register_message_handler(hs.country_where_live, state=UserAddState.country_where_live)
dp.register_message_handler(hs.email, state=UserAddState.email)

dp.register_message_handler(
    hs.add_user_photo,
    content_types=[types.ContentType.PHOTO, types.ContentType.TEXT],
    state=UserAddState.add_user_photo
)


# callbacks
dp.register_callback_query_handler(
    hs.get_info,
    lambda c: c.data=='info',
    state=UserAddState.user_language
)

dp.register_callback_query_handler(
    hs.set_user_data,
    lambda c: c.data=='register',
    state=UserAddState.user_language
)

# family status
dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'unmarried',
    state=UserAddState.process_user_family_status,
)
dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'married',
    state=UserAddState.process_user_family_status,
)
dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'divorced',
    state=UserAddState.process_user_family_status,
)
dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'widowed',
    state=UserAddState.process_user_family_status,
)
dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'legally separated',
    state=UserAddState.process_user_family_status,
)

# language select
dp.register_callback_query_handler(
    hs.welcome_message,
    lambda c: c.data == 'russian',
    state=UserAddState.user_language,
)

dp.register_callback_query_handler(
    hs.welcome_message,
    lambda c: c.data == 'kyrgyz',
    state=UserAddState.user_language,
)

# cancel
dp.register_callback_query_handler(
    hs.restart_bot,
    lambda c: c.data == 'cancel',
    state=UserAddState,
)

# back
dp.register_callback_query_handler(
    hs.set_user_data,
    lambda c: c.data == 'back_to_name',
    state=UserAddState,
)

# gender select
dp.register_callback_query_handler(
    hs.add_user_gender,
    lambda c: c.data == 'male',
    state=UserAddState.add_user_gender,
)

dp.register_callback_query_handler(
    hs.add_user_gender,
    lambda c: c.data == 'female',
    state=UserAddState.add_user_gender,
)

# eligibility
dp.register_callback_query_handler(
    hs.eligibility,
    lambda c: c.data == 'eligibility_yes',
    state=UserAddState.eligibility,
)

dp.register_callback_query_handler(
    hs.eligibility,
    lambda c: c.data == 'claiming_eligibility',
    state=UserAddState.eligibility,
)

# education
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'p_s_only',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'h_s_no_degree',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'h_s',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'v_s',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'some_u_courses',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'u_d',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 's_g_l_c',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'm_d',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 's_d_l_c',
    state=UserAddState.education_level,
)
dp.register_callback_query_handler(
    hs.education_level,
    lambda c: c.data == 'd_d',
    state=UserAddState.education_level,
)