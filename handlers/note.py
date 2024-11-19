from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from utils import keyboard as kb


router = Router()

@router.message()
async def add_task(msg: Message):
    await msg.answer('Заметки')