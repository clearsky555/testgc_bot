import os
import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from transliterate import translit
from googletrans import Translator


from bot_utils.keyboards import *

from state import UserAddState

from db.database import users_manager

translator = Translator()


async def restart_bot(callback: types.CallbackQuery, state):
    text = 'перезапуск бота'
    await callback.message.answer(text)
    await state.finish()
    await language_selection(callback.message)


# async def back_to_welcome_message(callback: types.CallbackQuery, state):
#     async with state.proxy() as data:
#         print(f'это вывод state data из back_to_welcome_message: {data}')
#         print(callback.data)
#     await UserAddState.user_language.set()
#     await welcome_message(callback, state)


async def language_selection(message: types.Message):
    text = 'Добрый день, я бот для регистрации на лотерею green card. Пожалуйста, выберите язык'
    markup = get_language_button()
    await message.answer(text, reply_markup=markup)

    await UserAddState.user_language.set()


async def welcome_message(callback: types.callback_query, state):
    async with state.proxy() as data:
        data['language'] = callback.data
        # print(data)
        # if callback.data != 'back':  # Update language only if callback.data is not 'back'
        #     data['language'] = callback.data
        # print(data)
    if callback.data == 'russian':
        text = 'язык установлен на русский'
    else:
        text = 'тил кыргызча болгондоо(кыргызский язык)'

    markup = get_menu_button(language=callback.data)
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
            Эртеңчи жана орнотпооңуз:
            
            Лотереяга үчүн жетишкен орто-мектептин жеткендери өтүү жеткиликтүү.
            
            Лотереяга үчүн жеткилишүүчү мамлекеттин өмүр калган адамдар, анын ичинде өмүр калган республиканын беренче кайсысында жашаганлар таттуу мүмкүн.
            
            Жардамкер болуу үчүн, биографиялык маалыматты камтыбашкалуу форма толтурулуп берилиш керек.
            
            Куштардын бардык жана 21 жашга чейинки балдарынын суреттери кирет.
            
            Жалааишы болбоо, АКШ виза-иммиграция эмес жасалган миграция кагаздарынын укуктарын жашыруу, социалдуу-кайрымтуу жана опасдуу кишкентайтуу жамааттык жазылууларды алууга чек.
            
            Кандайча үчүн керек?
            
            Калган маалыматты бул сылтамадан окуңуз:  http://greencard.by/lottery/rules/
                '''

    await callback.message.answer(text)


async def set_user_data(callback: types.CallbackQuery, state):
    async with state.proxy() as data:
        language = data['language']
        if language == 'russian':
            text = 'Пожалуйста, введите ваше имя (first_name)'
            back_text = 'Назад'
        else:
            text = 'Атыңызды киргизиниз(введите имя)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='cancel')
    markup = types.InlineKeyboardMarkup().add(back_button)

    await callback.message.answer(text, reply_markup=markup)

    await UserAddState.add_user_name.set()


async def add_user_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        name = message.text
        name = translit(name, language_code='ru', reversed=True)

        data['name'] = name
        print(data)
        language = data['language']
        if language == 'russian':
            text = 'введите вашу фамилию(last_name)'
            back_text = 'Назад'
        else:
            text = 'Тегерегиңизди киргизиңиз(введите фамилию)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')
    markup = types.InlineKeyboardMarkup().add(back_button)

    await message.answer(text, reply_markup=markup)

    await UserAddState.add_user_surname.set()


async def add_user_surname(message: Message, state:FSMContext):
    async with state.proxy() as data:
        surname = message.text
        surname = translit(surname, language_code='ru', reversed=True)
        data['surname'] = surname

        # middle_name = message.text
        # middle_name = translit(middle_name, language_code='ru', reversed=True)
        # data['middle_name'] = middle_name
        text = 'введите ваше отчество(middle_name)'
        back_text = 'Назад'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')
    markup = types.InlineKeyboardMarkup().add(back_button)

    await message.answer(text, reply_markup=markup)

    await UserAddState.add_user_middle_name.set()


async def add_user_middle_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        middle_name = message.text
        middle_name = translit(middle_name, language_code='ru', reversed=True)
        data['middle_name'] = middle_name
        text = 'укажите ваш пол(gender)'
        back_text = 'Назад'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')

    markup = get_gender_button().add(back_button)

    await message.answer(text, reply_markup=markup)
    await UserAddState.add_user_gender.set()


async def add_user_gender(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        gender = callback.data
        data['gender'] = gender

        language = data['language']
        if language == 'russian':
            text = 'укажите вашу страну'
            back_text = 'Назад'
        else:
            text = 'Өз улуттуу өлкөнү көрсөтүңүз(ваша страна)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')

    markup = types.InlineKeyboardMarkup().add(back_button)

    await callback.message.answer(text, reply_markup=markup)
    await UserAddState.add_country.set()


async def add_country(message: Message, state: FSMContext):
    async with state.proxy() as data:
        country = message.text
        country = translator.translate(country, src='ru', dest='en').text
        data['country'] = country
        language = data['language']
        if language == 'russian':
            text = 'укажите ваш город'
            back_text = 'Назад'
        else:
            text = 'шаарды киргизиңиз(ваш город)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')

    markup = types.InlineKeyboardMarkup().add(back_button)

    await message.answer(text, reply_markup=markup)
    await UserAddState.add_city.set()

    print('функция отработала')


async def add_city(message: Message, state: FSMContext):
    async with state.proxy() as data:
        city = message.text
        city = translator.translate(city, src='ru', dest='en').text
        data['city'] = city
        language = data['language']
        if language == 'russian':
            text = 'укажите вашу улицу'
            back_text = 'Назад'
        else:
            text = 'көчөңүздү киргизиңиз (ваша улица)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')

    markup = types.InlineKeyboardMarkup().add(back_button)
    await message.answer(text, reply_markup=markup)

    await UserAddState.add_street.set()


async def add_street(message: Message, state: FSMContext):
    async with state.proxy() as data:
        street = message.text
        street = translit(street, language_code='ru', reversed=True)
        data['street'] = street
        language = data['language']
        if language == 'russian':
            text = 'укажите ваше семейное положение'
            back_text = 'Назад'
        else:
            text = 'Тегерек жолуңузду белгилеңиз(ваше семейное положение)'
            back_text = 'Артка(назад)'

    back_button = types.InlineKeyboardButton(back_text, callback_data='back_to_name')

    markup = get_family_status_button(language=data['language']).add(back_button)
    await message.answer(text, reply_markup=markup)
    async with state.proxy() as data:
        data['awaiting_family_status'] = True
    await UserAddState.process_user_family_status.set()


async def process_user_family_status(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        family_status = callback.data
        data['family_status'] = family_status
        del data['awaiting_family_status']  # Убираем флаг ожидания
        language = data['language']
        if language == 'russian':
            text = 'отправьте вашу фотографию'
        else:
            text = 'Сурөтүңүздү жөнөтүңүз(фотография)'

    await callback.message.answer(f"Вы выбрали семейный статус: {family_status}")
    # text = 'Теперь отправьте изображение'
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
            country = data['country']
            city = data['city']
            street = data['street']
            middle_name = data['middle_name']
            gender = data['gender']

            unique_filename = str(uuid.uuid4())
            filename = f"{unique_filename}"

            user_directory = f"media/users/{telegram_user_id}/"
            os.makedirs(user_directory, exist_ok=True)

            photo_path = os.path.join(user_directory, filename)

            await message.photo[-1].download(destination_file=photo_path)

            photo_url = photo_path

            user_data = {
                'telegram_user_id': telegram_user_id,
                'name': name,
                'surname': surname,
                'middle_name': middle_name,
                'gender': gender,
                'photo_url': photo_url,
                'family_status': family_status,
                'country': country,
                'city': city,
                'street': street,
            }
            users_manager.record_user_in_db(user_data)
            await message.answer('Данные успешно записаны в базу данных!')
        except Exception as ex:
            print(ex)
            await state.finish()
            await message.answer('произошла ошибка, пожалуйста, перезапустите бота, нажав start...')

        finally:
            await state.finish()
            print('state остановлен')