from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class UserAddState(StatesGroup):
    add_user = State()
    add_user_name = State()
    add_user_surname = State()
    add_user_photo = State()