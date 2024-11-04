from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):
    def __init__(self, admin: str = 'SpicySad'):
        self.admin = admin
        
    async def __call__(self, msg: Message) -> bool:
        return msg.from_user.username == self.admin