# # from aiogram import Bot, Dispatcher
# # from decouple import config
# #
# #
# # bot = Bot(token="6865032004:AAE8WuPf5piTNz1XAA2nuEZ0p9-6JTG8Dbg", parse_mode="HTML")
# # dp = Dispatcher(bot=bot)
# # print(f"Bot: {bot}, Dispatcher: {dp}")
# # if hasattr(dp, 'bot'):
# #     print(f"DP's Bot: {dp.bot}")
# # else:
# #     print("DP doesn't have a direct bot attribute.")
# #
# #
#
#
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
#
# TOKEN = "6865032004:AAE8WuPf5piTNz1XAA2nuEZ0p9-6JTG8Dbg"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: Message):
#     await message.reply("Hello!")
#
# if __name__ == "__main__":
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)
