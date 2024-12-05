import asyncio

from aiogram import Dispatcher
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import SimpleEventIsolation

from create_bot import bot
from handlers import (
    start,
    test,
    ai
)
from utils.filter import IsAdminMiddleware
from utils.scheduler import start_scheduler



async def start_bot():
    start_scheduler()

async def stop_bot():
    pass

def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    # scene_registry = SceneRegistry(dispatcher)
    # scene_registry.add(task.TaskScene)
    # scene_registry.add(note.NoteScene)
    return dispatcher

async def main():
    dp = create_dispatcher()
    dp.include_routers(
        # test.router,
        start.router,
        ai.router,
        # change_room.router,
        # task.router,
        # note.router
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