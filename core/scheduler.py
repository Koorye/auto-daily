import schedule
from itertools import chain

from .mail import Mail


class Scheduler(object):
    def __init__(self, cfg):
        self.cfg = cfg.schedule
        self.tasks = [x(cfg) for x in self.cfg['queue']]
        self.sender = Mail(cfg)
        
    def run(self):
        schedule.every().day.at(self.cfg['time']).do(self.run_once)
        
    def run_once(self):
        results = [task.run() for task in self.tasks]
        results = list(chain(*results))
        self.sender.run(results)
        return