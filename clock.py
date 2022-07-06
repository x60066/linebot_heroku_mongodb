from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import urllib.request

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
def scheduled_job():
    print(f'{datetime.datetime.now().ctime()}')
    print('Success 1')
    url = "https://chtran.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)
        
    print('Success 2')

sched.start()