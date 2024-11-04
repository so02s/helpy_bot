import logging

from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)

# инициализация бота
bot = Bot(token=config('TOKEN_BOT'), default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
dp = Dispatcher()




# # функция для выхвата аргументов
# def extract_arg(arg):
#     return arg.split()[1:]

# # функция для вывода дел
# def list_task():
#     today = datetime.date.today()
#     dateList = []
#     dateList.append(today)
#     taskPrint = "Лист дел на " + str(dateList[0])
#     taskPrint += '\n\nДела: '
#     for i in range(len(task_list)):
#         taskPrint += '\n'
#         taskPrint += task_list[i]
#     return taskPrint

# # вывести список дел
# @bot.message_handler(commands=['дела'])
# def tasks(message):
#     now = datetime.datetime.now() 
#     if now.hour == 23:
#         del task_list[:]
#     bot.send_message(message.chat.id, list_task())

# # отметить готовым 
# @bot.message_handler(commands=['сделано']) # + <arv>
# def check_task(message):
#     index = int(extract_arg(message.text)[0]) #this is the second argument passed to the bot in the command that we're turning into an integer
#     index -= 1
#     task_list[index] += ' done' #adds the unicode tick to the list item
#     bot.send_message(message.chat.id, list_task())

# # добавить дело
# @bot.message_handler(commands=['добавить дело']) # + <str-дело> + <date>
# def add_task(message):
#     task, date = extract_arg(message.text)

