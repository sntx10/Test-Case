from aiogram import types
from .db_utils import aggregate_salaries
import json
from .settings import dp, bot


@dp.message()
async def handle_msg(message: types.Message):
    try:
        data = json.loads(message.text)
        dt_from = data["dt_from"]
        dt_upto = data["dt_upto"]
        group_type = data["group_type"]

        result = aggregate_salaries(dt_from, dt_upto, group_type)
        await message.answer(json.dumps(result, indent=4))
    except:
        await message.answer("Неправильный формат данных!")
