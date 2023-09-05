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
dp.register_message_handler(hs.welcome_message, commands=['start'])

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
)

dp.register_callback_query_handler(
    hs.set_user_data,
    lambda c: c.data=='register',
)