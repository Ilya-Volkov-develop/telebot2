from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

BOOK_TABLE_BTN=KeyboardButton('ЗАБРОНИРОВАТЬ СТОЛИК  🐂')
MENU_BTN=KeyboardButton('МЕНЮ 🥩')
ADDRESS_AND_TIME_BTN=KeyboardButton('АДРЕС И ВРЕМЯ РАБОТЫ 🕰️')
SITY_BTN=KeyboardButton('НАШ САЙТ 🌐')
COLLECTING_BTN=KeyboardButton('ПРОБКОВЫЙ СБОР 🥃')
STOCK_BTN=KeyboardButton('АКЦИИ 🔥')

BACK_BTN=InlineKeyboardButton('⬅️ВЕРНУТЬСЯ',callback_data='back')

MENU_ADDRESS1=InlineKeyboardButton('СТРАСТНОЙ БУЛЬВАР, НОВОСЛОБОДСКАЯ, ПРОФСОЮЗНАЯ...',callback_data='address1')
MENU_ADDRESS2=InlineKeyboardButton('ДУШИНСКАЯ, Б.ТУЛЬСКАЯ',callback_data='address2')

MAIN_BTNS=ReplyKeyboardMarkup(one_time_keyboard=True).add(BOOK_TABLE_BTN).add(MENU_BTN).row(ADDRESS_AND_TIME_BTN,SITY_BTN).row(COLLECTING_BTN,STOCK_BTN)
MENU_BTNS=InlineKeyboardMarkup(one_time_keyboard=True).add(BACK_BTN).add(MENU_ADDRESS1).add(MENU_ADDRESS2)
BACK_BTNS=InlineKeyboardMarkup().add(BACK_BTN)