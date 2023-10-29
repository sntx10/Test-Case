import json
from bot.db_utils import aggregate_salaries
from aiogram.types import Message

from config import bot, dp
from decouple import config

import logging

logging.basicConfig(filename='bot.log', level=logging.INFO)


YOUR_CHAT_ID = config('YOUR_CHAT_ID')


async def on_startup(dp):
    await bot.send_message(chat_id=YOUR_CHAT_ID, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=YOUR_CHAT_ID, text='Bot has been stopped')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Hello!")


@dp.message_handler()
async def handle_json_query(message):
    logging.info(f"Received message: {message.text}")
    try:
        data = json.loads(message.text)
        dt_from = data["dt_from"]
        dt_upto = data["dt_upto"]
        group_type = data["group_type"]

        result = aggregate_salaries(dt_from, dt_upto, group_type)
        await message.answer(json.dumps(result, indent=4))

    except json.JSONDecodeError:
        await message.answer("Ошибка: Ваш запрос не является правильным JSON.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
