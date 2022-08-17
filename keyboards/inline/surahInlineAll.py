from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from parsings.surahParsing import get_surah_id
from parsings.surahAll_id import surahAll1,surahAll2,surahAll3,surahAll4,surahAll5,surahAll6

# callback_data
kirish_surah = CallbackData('surahs', 'item_name')


surahParsing1 = surahAll1


# Surah Inline All 1 inline keyboard
surahsMenu1 = InlineKeyboardMarkup(row_width=4)
for key, value in surahParsing1.items():
    surahsMenu1.insert(InlineKeyboardButton(
        text=key, callback_data=kirish_surah.new(item_name=value)))



ikkichi_surah = CallbackData('surahs', 'item_name')


surahParsing2 = surahAll2


# Surah Inline All 2 inline keyboard
surahsMenu2 = InlineKeyboardMarkup(row_width=3)
for key, value in surahParsing2.items():
    surahsMenu2.insert(InlineKeyboardButton(
        text=key, callback_data=ikkichi_surah.new(item_name=value)))


surah_callback3 = CallbackData('surah', 'item_name')


surahParsing3 = surahAll3


# Surah Inline All 3 inline keyboard
surahsMenu3 = InlineKeyboardMarkup(row_width=3)
for key, value in surahParsing3.items():
    surahsMenu3.insert(InlineKeyboardButton(
        text=key, callback_data=surah_callback3.new(item_name=value)))


# Surah Inline All 4 inline keyboard

surah_callback4 = CallbackData('surah', 'item_name')


surahParsing4 = surahAll4


# Surah Inline All 4 inline keyboard
surahsMenu4 = InlineKeyboardMarkup(row_width=3)
for key, value in surahParsing4.items():
    surahsMenu4.insert(InlineKeyboardButton(
        text=key, callback_data=surah_callback4.new(item_name=value)))


surah_callback5 = CallbackData('surah', 'item_name')


surahParsing5 = surahAll5


# Surah Inline All 5 inline keyboard
surahsMenu5 = InlineKeyboardMarkup(row_width=3)
for key, value in surahParsing5.items():
    surahsMenu5.insert(InlineKeyboardButton(
        text=key, callback_data=surah_callback5.new(item_name=value)))


surah_callback6 = CallbackData('surah', 'item_name')


surahParsing6 = surahAll6


# Surah Inline All 6 inline keyboard
surahsMenu6 = InlineKeyboardMarkup(row_width=3)
for key, value in surahParsing6.items():
    surahsMenu6.insert(InlineKeyboardButton(
        text=key, callback_data=surah_callback6.new(item_name=value)))



if __name__ == '__main__':
    print(surahParsing1)
    print(surahParsing2)
    print(surahParsing3)
    print(surahParsing4)
    print(surahParsing5)
    print(surahParsing6)
