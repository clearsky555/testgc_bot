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

dp.register_callback_query_handler(
    hs.process_user_family_status,
    lambda c: c.data == 'single',
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
    hs.welcome_message,
    lambda c: c.data == 'russian',
    state=UserAddState.user_language,
)

dp.register_callback_query_handler(
    hs.welcome_message,
    lambda c: c.data == 'kyrgyz',
    state=UserAddState.user_language,
)

dp.register_callback_query_handler(
    hs.restart_bot,
    lambda c: c.data == 'cancel',
    state=UserAddState,
)

# dp.register_callback_query_handler(
#     hs.back_to_welcome_message,
#     lambda c: c.data == 'back',
#     state=UserAddState,
# )

dp.register_callback_query_handler(
    hs.set_user_data,
    lambda c: c.data == 'back_to_name',
    state=UserAddState,
)