from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class UserAddState(StatesGroup):
    add_user = State()
    add_user_name = State()
    add_user_surname = State()
    add_user_middle_name = State()
    add_user_gender = State()
    add_birth_date = State()
    add_birth_city = State()
    add_birth_country = State()
    eligibility = State()
    process_user_family_status = State()
    add_user_photo = State()
    user_language = State()
    add_country = State()
    add_city = State()
    add_street = State()
    country_where_live = State()
    email = State()
    education_level = State()