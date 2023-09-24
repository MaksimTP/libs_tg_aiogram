from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from os import listdir
from random import randint
import json

print('Initialize keyboard module')

def get_random_files(list_of_json_files = listdir('12_libs_artem\data')):
    '''
    Эта функция возвращает список из 5 элементов. Этими элементами являются
    названия пяти файлов json формата
    '''
    random_indxs_list = []
    for i in range(5):
        rand = randint(0,4999)
        random_indxs_list.append(rand)
    five_filenames_json = []
    for indx in random_indxs_list:
        five_filenames_json.append(list_of_json_files[indx])
    return five_filenames_json


def func_to_get_file_info(random_filenames_list):
    '''
    Эта функция по сути принимает список, который возвращает функция get_random_files. Здесь мы забираем всю информацию для дальнейшего наполнения ТГ бота
    '''
    file_info_list = []
    for filename in random_filenames_list:
        with open(f'12_libs_artem\data\{filename}', 'r', encoding = 'utf-8') as file:
            file_info = json.load(file)
            file_info_list.append(file_info)

    return file_info_list


# print(list_of_json_files[:100])
# print(len(list_of_json_files))

def build_random_files_keyboard(random_filenames_list: list[str]) -> ReplyKeyboardMarkup:
    '''
    Это функция опять же принимает список, который возвращает функция get_random_files. Здесь мы получаем клавиатуру
    состоящую из 5 кнопок, их значения = названия полученных библиотек.
    '''
    # list_of_json_files = listdir('12_libs_artem\data')
    file_info_list = []

    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton]= []

    # random_filenames_list: list[str] = get_random_files(list_of_json_files)

    file_info_list = func_to_get_file_info(random_filenames_list)

    buttons = [KeyboardButton(text=file['project']) for file in file_info_list]
    kb_builder.row(*buttons, width = 2)

    return kb_builder.as_markup(resize_keyboard = True)


yes_no = ['Да', "Не хочу"]
kb_builder_yes_no: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: KeyboardButton = [KeyboardButton(text = i) for i in yes_no ]

kb_builder_yes_no.row(*buttons)

keyboard_yes_no: ReplyKeyboardMarkup = kb_builder_yes_no.as_markup(resize_keyboard = True)


aftermath = ['Конечно!', "Да не особо"]

kb_builder_aftermath: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: KeyboardButton = [KeyboardButton(text = i) for i in aftermath]

kb_builder_aftermath.row(*buttons)

keyboard_aftermath: ReplyKeyboardMarkup = kb_builder_aftermath.as_markup(resize_keyboard = True)