from typing import Any, Awaitable, Callable, Dict

from aiogram.filters import BaseFilter
from aiogram.types import Message, TelegramObject
from aiogram.filters.callback_data import CallbackData
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from utils.globals import Globals

# Я НАШЛА
# ВНИМАНИЕ, ЕСТЬ ЕЩЕ CancelHandler в этом модуле
# П. с. АЗАХАХАХАХХА ОНИ ВНУТРИ ПРОПИСАНЫ КАК pass ПОЧЕМУУУУУ
from aiogram.dispatcher.event.bases import SkipHandler

class RoomCallbackFactory(CallbackData, prefix="fabroom"):
    room_name: str
    
# TODO admin в настройках
class IsAdminMiddleware(BaseMiddleware):  
    def __init__(self, admin: str = 'SpicySad'):
        super().__init__()
        self.admin = admin
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict
    ) -> Any:
        
        if event.from_user.username != self.admin:
            await event.answer('[Нажми меня](https://www.youtube.com/watch?v=oHg5SJYRHA0)', parse_mode = "Markdown", link_preview=False, disable_web_page_preview=True)
            return
        
        return await handler(event, data)

# ---------- Фильтр для комнат
# TODO пока не работает
# по какой-то причине тут tg объект
class RoomFilter(BaseFilter):
    def __init__(self, room_name: str):
        self.room_name = room_name
    
    async def __call__(self, room_name: str) -> bool:
        if Globals().room_now == room_name:
            return True
        print(f"{Globals().room_now}\n\n{room_name}")
        return False



class RoomMiddleware(BaseMiddleware):
    def __init__(self, room_name: str = ''):
        super().__init__()
        self.room_name = room_name
    
    # async def on_process_message(self, message: Message, data: dict):
    #     if Globals().room_now != self.required_room:
    #         # await message.answer("Вы не находитесь в нужной комнате.")
    #         return False
    #     return True
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict
    ) -> Any:
        if Globals().room_now != self.room_name:
            print("FUCK")
            raise SkipHandler()
            # TODO ТУТ должен быть пржок через роутер
            # мб пытаюсь натянуть сову на глобус, посмотрю как сделать по-другому
            # raise SkipRouter()
            # pass
        return await handler(event, data)