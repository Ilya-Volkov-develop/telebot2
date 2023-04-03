import keyboards
import messages
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=os.environ.get('BOT_API_TOKEN'), proxy=PROXY_URL)
dp = Dispatcher(bot)


#start
@dp.message_handler(commands=['start', 'c'])
async def started_message(message: types.Message):
    await message.answer(text=messages.hello(), reply_markup=keyboards.MAIN_BTNS)


#обработка кнопки "меню"
@dp.message_handler(text='МЕНЮ 🥩')
async def menu_message(message: types.Message):
    await message.answer(text=messages.choose_restaurant(), reply_markup=keyboards.MENU_BTNS)

#обработка кнопки "АДРЕС И ВРЕМЯ РАБОТЫ"
@dp.message_handler(text='АДРЕС И ВРЕМЯ РАБОТЫ 🕰️')
async def address_message(message: types.Message):
    await message.answer(text=messages.message_address(), reply_markup=keyboards.BACK_BTNS)

#обработка кнопки "НАШ САЙТ"
@dp.message_handler(text='НАШ САЙТ 🌐')
async def site_message(message: types.Message):
    await message.answer(text=messages.message_site_link(), reply_markup=keyboards.BACK_BTNS)


#обработка кнопки "ПРОБКОВЫЙ СБОР"
@dp.message_handler(text='ПРОБКОВЫЙ СБОР 🥃')
async def collecting_message(message: types.Message):
    await message.answer(text=messages.message_collecting(), reply_markup=keyboards.BACK_BTNS)

#обработка кнопки "АКЦИИ"
@dp.message_handler(text='АКЦИИ 🔥')
async def collecting_message(message: types.Message):
    await message.answer(text=messages.message_stock(), reply_markup=keyboards.BACK_BTNS)


@dp.callback_query_handler(text='back')
async def menu_message_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.hello(),
        reply_markup=keyboards.MAIN_BTNS)


@dp.callback_query_handler(text='address1')
async def dialog_address1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(
        callback_query_id=callback_query.id,
        text="https://str.thebull.ru/takeout",
        show_alert=True)


@dp.callback_query_handler(text='address2')
async def dialog_address2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(
        callback_query_id=callback_query.id,
        text="https://msk.thebull.ru/takeout/",
        show_alert=True)


executor.start_polling(dp, skip_updates=True)