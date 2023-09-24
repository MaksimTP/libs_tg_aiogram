from aiogram import Router
from aiogram.filters import Text,Command
from aiogram.types import Message
from keyboards import *

router: Router = Router()

# listdir() - функция для просмотра каталога. Аргумент: путь к расположению директории. Возвращает - список имен файлов и папок, которые она содержит.

user_template: dict = {
    'filenames': None,
    'download_count': [],
    'project': [],
    'url': [],
    'description': [],
    'choice_ind': -20
}


user_db: dict = {
    'filenames': None,
    'download_count': [],
    'project': [],
    'url': [],
    'description': [],
    'choice_ind': -20
}


# Сюда добавить клавиатуру, которая предложит сыграть в игру. Будет две кнопки: "ДА" и "НЕТ"
@router.message(Command(commands='start'))
async def process_start_message(message: Message):
    await message.answer('Привет! Здесь будет объяснение по функционалу бота', reply_markup = keyboard_yes_no)

@router.message(Text(text='Да'))
async def process_yes_btn(message: Message):

    five_filenames_json = get_random_files()
    kb = build_random_files_keyboard(five_filenames_json)

    user_db['filenames'] = five_filenames_json
    print(user_db['filenames'])

    file_info_list = func_to_get_file_info(five_filenames_json)
    for file in file_info_list:
        user_db['download_count'].append(file['download_count'])
        user_db['project'].append(file['project'])
        user_db['url'].append(file['url'])
        user_db['description'].append(file['description'])

    await message.answer("Отлично! Погнали", reply_markup=kb)


@router.message(Text(text='Не хочу'))
async def process_no_btn(message: Message):
    await message.answer("Очень жаль! Если хочешь потом поиграть, то смело пиши /start!", reply_markup=ReplyKeyboardRemove())






@router.message(lambda message: message.text in user_db['project'])
async def process_answer(message: Message):
    await message.answer(f'Окей, ты хочешь узнать о библиотеке {message.text}, тогда держи инфу!')

    indx_of_projectname_in_db = user_db['project'].index(message.text)

    user_db['choice_ind']=indx_of_projectname_in_db
    # j = 2
    # while len(user_db['description']) > 1 and user_db['description'][j-2:j][indx_of_projectname_in_db] == '\n':
    #     user_db['description'][j][indx_of_projectname_in_db] = ''
    #     j += 1

    await message.answer(f"Библиотека: {user_db['project'][indx_of_projectname_in_db]}\n\nКоличество скачиваний: {user_db['download_count'][indx_of_projectname_in_db]}\n\nСсылка на библиотеку: {user_db['url'][indx_of_projectname_in_db]}\n\nНазначение библиотеки: {user_db['description'][indx_of_projectname_in_db][:600]}.......")

    await message.answer(f'Хочешь посмотреть информацию по остальным библиотекам?', reply_markup = keyboard_aftermath)


@router.message(Text(text='Конечно!'))
async def process_yes_aftermath(message: Message):
    # choice = user_db['']
    for i in range(5):
        if user_db['choice_ind'] != i:
            # j = 2
            # while user_db['description'][j-2:j][i] == '\n':
            #     user_db['description'][][i] = ''
            #     j += 1
            # while '\n\n' in user_db['description'][:600][i]:
            #     x = user_db['description'][i].replace('\n\n', '')
            #     print(x)
            await message.answer(f"Библиотека: {user_db['project'][i]}\n\nКоличество скачиваний: {user_db['download_count'][i]}\n\nСсылка на библиотеку: {user_db['url'][i]}\n\nНазначение библиотеки: {user_db['description'][i][:600]}.......")

    for item_1,item_2 in zip(user_db.keys(),user_template.keys()):
        user_db[item_1] = user_template[item_2]

    # user_db = user_template.copy()
    await message.answer('Нажмите на /start, если хотите еще библиотек', reply_markup=ReplyKeyboardRemove())


@router.message(Text(text='Да не особо'))
async def process_no_aftermath(message: Message):
    # user_db = user_template.copy()

    for item_1,item_2 in zip(user_db.keys(),user_template.keys()):
        user_db[item_1] = user_template[item_2]



    await message.answer("Очень жаль! Если хочешь потом поиграть, то смело пиши /start!", reply_markup=ReplyKeyboardRemove())


