import os
import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot_utils.keyboards import get_menu_button, get_family_status_button, get_language_button

from state import UserAddState

from db.database import users_manager


async def language_selection(message: types.Message):
    text = 'Добрый день, я бот для регистрации на лотерею green card. Пожалуйста, выберите язык'
    markup = get_language_button()
    await message.answer(text, reply_markup=markup)

    await UserAddState.user_language.set()


async def welcome_message(callback: types.callback_query, state):
    async with state.proxy() as data:
        data['language'] = callback.data
        print(data)
    if callback.data == 'russian':
        text = 'язык установлен на русский'
    else:
        text = 'кыргыз тили'
    markup = get_menu_button()
    await callback.message.answer(text, reply_markup=markup)


async def get_info(callback: types.callback_query, state):
    async with state.proxy() as data:
        language = data['language']
        if language == 'russian':
            text = '''
            Коротко и просто:
    
            Чтобы участвовать в лотерее, достаточно иметь среднее образование.
            Участвовать могут уроженцы почти всех стран, в том числе и все, кто родился на территории республик бывшего СССР.
            Чтобы стать участником, нужно заполнить анкету с указанием биографических сведений.
            К анкете требуются фотографии всех членов семьи (супруги и дети до 21 года).
            Не быть судимым, не нарушать визово-иммиграционные законы США, не иметь социально-опасных заболеваний.
            Что необходимо для участия?
    
                Остальная информация по ссылке: http://greencard.by/lottery/rules/
                '''
        else:
            text = '''
            Информация на кыргызском
            Коротко и просто:

            Чтобы участвовать в лотерее, достаточно иметь среднее образование.
            Участвовать могут уроженцы почти всех стран, в том числе и все, кто родился на территории республик бывшего СССР.
            Чтобы стать участником, нужно заполнить анкету с указанием биографических сведений.
            К анкете требуются фотографии всех членов семьи (супруги и дети до 21 года).
            Не быть судимым, не нарушать визово-иммиграционные законы США, не иметь социально-опасных заболеваний.
            Что необходимо для участия?

                Остальная информация по ссылке: http://greencard.by/lottery/rules/
                '''

    await callback.message.answer(text)


async def set_user_data(callback: types.CallbackQuery, state):
    async with state.proxy() as data:
        language = data['language']
        if language == 'russian':
            text = 'Пожалуйста, введите ваше имя'
        else:
            text = 'Атыңызды киргизиниз'
    await callback.message.answer(text)
    await UserAddState.add_user_name.set()


async def add_user_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    text = 'Теперь введите вашу фамилию'
    await message.answer(text)
    await UserAddState.add_user_surname.set()


async def add_user_surname(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    text = 'Теперь отправьте семейное положение'
    # await UserAddState.add_user_family_status.set()

    markup = get_family_status_button()

    await message.answer(text, reply_markup=markup)
    async with state.proxy() as data:
        data['awaiting_family_status'] = True
    await UserAddState.process_user_family_status.set()

    print('функция отработала')


async def process_user_family_status(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        family_status = callback.data
        data['family_status'] = family_status
        del data['awaiting_family_status']  # Убираем флаг ожидания

    await callback.message.answer(f"Вы выбрали семейный статус: {family_status}")
    text = 'Теперь отправьте изображение'
    await callback.message.answer(text)

    await UserAddState.add_user_photo.set()


async def add_user_photo(message: Message, state: FSMContext):
    print('функция выбора фото запустилась')
    async with state.proxy() as data:
        data['photo'] = message.photo[-1]

        try:
            users_manager.create_table()
            telegram_user_id = message.from_user.id
            name = data['name']
            surname = data['surname']
            family_status = data['family_status']

            unique_filename = str(uuid.uuid4())
            filename = f"{unique_filename}"

            user_directory = f"media/users/{telegram_user_id}/"
            os.makedirs(user_directory, exist_ok=True)

            photo_path = os.path.join(user_directory, filename)

            await message.photo[-1].download(destination_file=photo_path)

            photo_url = photo_path

            user_data = {'telegram_user_id': telegram_user_id, 'name': name, 'surname': surname, 'photo_url': photo_url, 'family_status': family_status}
            users_manager.record_user_in_db(user_data)
            await message.answer('Данные успешно записаны в базу данных!')
        except Exception as ex:
            print(ex)
            await message.answer('произошла ошибка, пожалуйста, перезапустите бота, нажав start...')

        finally:
            await state.finish()
            print('state остановлен')