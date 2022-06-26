from main import *
from admin import *
from loader import db
from aiogram import executor
if __name__ == "__main__":
    executor.start_polling(db,skip_updates=True)