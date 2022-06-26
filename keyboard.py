from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
from datafetcher import give_get
from aiogram.utils.callback_data import CallbackData
edit_chanel = CallbackData('r','id')
edit_chanel1 = CallbackData('t','id')

async def yana_tugatish():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    mark_up.add(
        KeyboardButton(text='Yana id qo`shish'),
        KeyboardButton(text='Tugatish')
    )
    return mark_up


async def give_mark():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    data = await give_get()
    for i in data:
        print(i)
        tugma = KeyboardButton(text=f'{i["name"]}')
        mark_up.add(tugma)
    return mark_up
async def end_key():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    tugma = KeyboardButton(text='Tugatish')
    mark_up.add(tugma)
    return mark_up

async def give_name(name):
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    tugma = KeyboardButton(text=name)
    mark_up.add(tugma)
    return mark_up

async def statistics():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tugma = KeyboardButton(text='Statistika')
    tugma1 = KeyboardButton(text='Kanallar')
    tugma4 = KeyboardButton(text='Kanal qo`shish')
    tugma6 = KeyboardButton(text='GIVE-ning vaqtini belgilash')
    tugma2 = KeyboardButton(text='Elon yuborish')
    tugma3 = KeyboardButton(text='Give o`tqizish')
    tugma5 = KeyboardButton(text='Tushuntirib berish')
    mark_up.add(tugma,tugma1,tugma4,tugma2)
    mark_up.add(tugma6)
    mark_up.add(tugma3,tugma5)
    return mark_up

async def xabar():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tugma = KeyboardButton(text='Birkishiga')
    tugma1 = KeyboardButton(text='Xammaga')
    mark_up.add(tugma,tugma1)
    return mark_up

async def edit_channel(id):
    mark =InlineKeyboardMarkup(row_width=1)
    tugma = InlineKeyboardButton(text='O`chirish',callback_data=f'r:{id}')
    mark.add(tugma)
    return mark


async def check_sub(id):
    mark =InlineKeyboardMarkup(row_width=1)
    tugma = InlineKeyboardButton(text='Tekshirish',callback_data=f't:{id}')
    mark.add(tugma)
    return mark


async def otish():
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tugma = KeyboardButton(text='Asosiy kanalga o`tish')
    tugma1 = KeyboardButton(text='Asosiy grupaga o`tish')
    tugma_s = KeyboardButton(text='Statistika')
    tugma2 = KeyboardButton(text='Biz xaqimizda')
    tugma3 = KeyboardButton(text='GIVEni o`tqizish vaqti')
    mark_up.add(tugma,tugma1)
    mark_up.add(tugma_s)
    mark_up.add(tugma2,tugma3)
    return mark_up