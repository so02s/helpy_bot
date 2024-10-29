from codecs import utf_32_be_decode
# -*- coding: utf_32_be_decode -*-

import telebot # собственно, бот
import datetime # для привязки ко времени
from config import host, user, password, db_name, port
# import sqlalchemy

'''
Пока - синхронные функции, так как работаю с ботом только я
Позже можно будет задуматься над ассинхронкой
'''


# токен для бота
token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if(message.text == "Привет!"):
        bot.reply_to(message, "Приветики!")
    elif(message.text == "Как дела?"):
        bot.reply_to(message, "Нормально")

# а это - sqlalchemy
# engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
# try:
#     engine.connect()
# except Exception as _ex:
#     print("[INFO] Error while working with PostgreSQL", _ex)

# Base = declarative_base()

# class Task(Base):
#     __tablename__ = 'tasks'
#     id = Column(Integer, primary_key=True)
#     task = Column(String(200), nullable=False)
#     time_from = Column(Time())
#     date = Column(Date())
#     done = Column()


# task_list = []


# # просто я
# admin = 'SpicySad'

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

bot.infinity_polling() #постоянная проверка сообщений, пока прога активна
