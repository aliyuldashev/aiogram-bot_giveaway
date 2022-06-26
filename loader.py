from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import data as config
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
db = Dispatcher(bot, storage=storage)