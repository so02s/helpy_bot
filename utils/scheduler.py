import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.obsidian import timetable

'''
    Модуль реализующий напоминания. За час напоминает о деле.
    Утром и вечером отправляет расписание на этот/следующий день.
'''

# TODO возможность добавить будильник за 10 мин

def start_scheduler():
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(timetable, 'cron', hour=20, minute=0)
    # scheduler.add_job(timetable, 'cron', hour=8, minute=15)
    # scheduler.add_job(send_reminders, trigger=IntervalTrigger(hours=1))
    scheduler.start()
    return scheduler

# TODO
async def send_reminders():
    # Проверить файловую систему (ФС) на разные таски
    
    # Тыкнуть ИИ на генерацию нормального уведомления
    
    # Отправить уведомления
    
    
    pass