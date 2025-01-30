from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.start()
    trigger = CronTrigger(
        year="*", month="*", day="*", hour="19", minute="10", second="0"
    )
    scheduler.add_job(
        
        trigger=trigger,
        name="daily foo"
    )
