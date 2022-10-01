import schedule
import time
from core import Scheduler
from config import MyConfig, BabyConfig


Scheduler(MyConfig()).run(instantly=True)
schedulers = [Scheduler(cfg()) for cfg in [MyConfig, BabyConfig]]
for sch in schedulers:
    sch.run()
print('Script is running NOW!')
    
while True:
    schedule.run_pending()
    time.sleep(1)
