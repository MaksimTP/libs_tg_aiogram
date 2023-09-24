from aiogram import Bot, Dispatcher
import asyncio
from config import TOKEN_NAME
import user_handlers

async def main():

    dp: Dispatcher = Dispatcher()
    bot: Bot = Bot(token=TOKEN_NAME)

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())