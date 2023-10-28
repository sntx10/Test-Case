from aiogram import Bot, Dispatcher
from decouple import config

API_TOKEN = config("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

MONGO_USERNAME = config("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = config("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DB = config("MONGO_INITDB_DATABASE")


