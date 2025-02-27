from typing import Any, Awaitable, Callable, Dict

from aiogram.types import TelegramObject
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from decouple import config

class IsAdminMiddleware(BaseMiddleware):  
    def __init__(self, admin: str = config("ADMIN_NAME")):
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