import asyncio
import aiofiles
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from decouple import config
from datetime import datetime, timedelta
from create_bot import bot
from utils import promt, obsidian as obs
from handlers import ai

'''
    Модуль реализующий напоминания. За час напоминает о деле.
    Утром и вечером отправляет расписание на этот/следующий день.
'''

# TODO возможность добавить будильник за 10 мин

def start_scheduler():
    scheduler = AsyncIOScheduler()
    
    # Функция-обертка для передачи текущей даты
    def schedule_timetable_current():
        current_date = datetime.now().strftime('%Y-%m-%d')
        scheduler.add_job(obs.timetable, args=[current_date])
    
    # Функция-обертка для передачи следующей даты
    def schedule_timetable_next():
        next_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        scheduler.add_job(obs.timetable, args=[next_date])
    
    scheduler.add_job(schedule_timetable_current, 'cron', hour=20, minute=0)
    scheduler.add_job(schedule_timetable_next, 'cron', hour=8, minute=15)
    scheduler.add_job(send_reminders, trigger=IntervalTrigger(hours=1))
    scheduler.start()
    return scheduler

async def send_reminders():
    # Проверить файловую систему (ФС) на разные таски
    tasks_folder = './Time'
    
    today = datetime.now().strftime('%Y-%m-%d')
    today_path = os.path.join(tasks_folder, today)
    
    if not os.path.exists(today_path):
        return
    
    async with aiofiles.open(today_path, 'r', encoding='utf-8') as file:
        tasks = await file.readlines()
    
    now = datetime.now()
    
    reminders = ''
    
    for task in tasks:
        if not task.startswith("- [ ]"):
            continue
        
        task = task.lstrip("- [ ] ")
        parts = task.strip().split(' ')
        
        time_range = parts[0]
        name = ' '.join(parts[1:])
        
        # Разделяем время начала и конца
        start_str, end_str = time_range.split('-')
        task_start = datetime.strptime(start_str, '%H:%M')
        
        # Привязываем время задачи к текущей дате
        task_start = task_start.replace(year=now.year, month=now.month, day=now.day)
        
        # Проверяем, осталось ли до начала задачи менее одного часа
        if now <= task_start <= now + timedelta(hours=1):
            reminders += (f"{name} - {task_start.strftime('%H:%M')}\n")
    
    # Тыкнуть ИИ на генерацию нормального уведомления
    text = await ai.ask(reminders, instructions=promt.good_answer())
    
    # Отправить уведомления
    await bot.send_message(config('ADMIN_ID'), text)