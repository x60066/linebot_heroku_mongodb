from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import urllib

sched = BlockingScheduler()

@sched.scheduled_job('cron',  minute='*/2')
def scheduled_job():
    print(f'{datetime.datetime.now().ctime()}')
    url = "https://chtran.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()