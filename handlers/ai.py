from aiogram import Router, F


router = Router()













































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