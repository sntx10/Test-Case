from aiogram import executor
from bot.handlers import on_startup, on_shutdown
from config import dp

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
