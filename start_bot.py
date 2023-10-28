from bot.settings import dp, bot

if __name__ == '__main__':
    import asyncio

    asyncio.run(dp.start_polling(bot))


