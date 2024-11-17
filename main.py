import asyncio

from create_bot import bot, dp
from handlers import (
    start,
    task,
    change_room
)
from utils.filter import IsAdminMiddleware

async def start_bot():
    pass

async def stop_bot():
    pass

async def main():
    dp.include_routers(
        start.router,
        task.router,
        change_room.router
    )
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.outer_middleware(IsAdminMiddleware())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())