from core import Scheduler
from config import MyConfig


sch = Scheduler(MyConfig())
sch.run_once()