from aiogram import Router, F
from aiogram.types import Message
import requests # grequests as 
from utils import promt
from handlers.note import project

router = Router()

@router.message()
async def gui_ai(msg: Message):
    text = await ask(msg.text)
    # TODO проверка на правильность JSON формата. Если нет - попробовать еще два раза
    await msg.answer(text)


def random_id_generator():
    import uuid
    return str(uuid.uuid4())

# Запрос к ИИ
async def ask(
    req: str,
    instructions: str = promt.func_call(),
    url: str = 'https://www.blackbox.ai/api/chat'
):
    data = {
        "messages": [{"id": "2wlAo5V", "content": f"{instructions}\n\n---\n\n{req}", "role": "user"}],
        "id": "2wlAo5V",
        "previewToken": None,
        "userId": random_id_generator(),
        "codeModelMode": True,
        "agentMode": {},
        "trendingAgentMode": {},
        "isMicMode": False,
        "isChromeExt": False,
        "githubToken": None,
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "visitFromURL": None
    }
    
    response = requests.post(url, json=data, stream=True)
    sources = None
    resp = ""

    for text_stream in response.iter_lines(decode_unicode=True, delimiter="\n"):
        if sources is None: sources = text_stream
        else: resp += text_stream + "\n"
        
    return resp

































# from openai import OpenAI

# from aiogram import Router, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
# from aiogram.types.callback_query import CallbackQuery

# from create_bot import bot
# from utils.filter import IsAdmin
# from utils import keyboard as kb

# router = Router()

# dialog_history = []

# client = OpenAI(
#     base_url='http://localhost:11434/v1',
#     api_key='ollama',
# )

# @router.message(IsAdmin())
# async def start_cmd(msg: Message):
#     global dialog_history
#     user_input = msg.text

#     if user_input.lower() == "stop":
#         await msg.answer("Диалог завершен. Спасибо за общение!")
#         dialog_history = []
#         return

#     dialog_history.append({
#         "role": "user",
#         "content": user_input,
#     })

#     response = client.chat.completions.create(
#         model="llama2",
#         messages=dialog_history,
#     )

#     response_content = response.choices[0].message.content
#     await msg.answer(response_content)

#     dialog_history.append({
#         "role": "assistant",
#         "content": response_content,
#     })