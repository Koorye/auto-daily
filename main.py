import schedule
import time
from core import Scheduler
from config import MyConfig, BabyConfig


schedulers = [Scheduler(cfg()) for cfg in [MyConfig, BabyConfig]]
for sch in schedulers:
    sch.run()
    
while True:
    schedule.run_pending()
    time.sleep(1)
