from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from create_bot import bot
from utils import keyboard as kb


import requests
import re
from typing import Tuple, Optional

def generate(prompt: str, system_prompt: str = " Don't Write Code unless Mentioned", stream: bool = True, chat_endpoint: str = "https://www.blackbox.ai/api/chat") -> Tuple[Optional[str], str]:

    payload = {
        "messages": [{"content": prompt, "role": "user"}],
        # "messages": [{"content": system_prompt, "role": "system"}, {"content": prompt, "role": "user"}],
        "agentMode": {},
        "trendingAgentMode": {},
    }

    response = requests.post(chat_endpoint, json=payload, stream=True)

    sources = None
    resp = ""

    for text_stream in response.iter_lines(decode_unicode=True, delimiter="\n"):
        if text_stream:
            if sources is None: sources = text_stream
            elif stream: resp += text_stream + "\n"

    return sources, resp

def split_text(text, max_length=4000):
    """Разбивает текст на части, каждая из которых не превышает max_length символов."""
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


'''
    Небольшое тестовое пространство
'''

router = Router()

@router.message()
async def start_console(msg: Message):
    sources, resp = generate(msg.text, stream=True)
    # print(resp)
    await msg.answer(sources, resp)