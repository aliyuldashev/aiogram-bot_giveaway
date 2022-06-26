from aiogram.dispatcher.filters.state import StatesGroup, State

class Admin(StatesGroup):
    nomi = State()
    linklar = State()
    yana = State()
    time = State()
    kutish = State()
    kutish_2 = State()

class Edit(StatesGroup):
    edit =State()

class Elon(StatesGroup):
    kutish = State()
    xamaga = State()
    bir = State()
    bir_id = State()

class User(StatesGroup):
    give =State()
    patpiska = State()
    tekshirish = State()
    otish = State()