import datetime

from .utils import parse_html


class Dairy(object):
    def __init__(self, cfg):
        self.cfg = cfg.dairy
        
    def run(self):
        today = datetime.date.today()
        birthday = self.cfg['birthday']
        year, month, day = [int(x) for x in birthday.split('-')]
        birthday = datetime.date(year, month, day)
        spawn_days = (today - birthday).days

        birthday = datetime.date(today.year, month, day)
        if birthday < today:
            birthday = datetime.date(today.year + 1, month, day)
        next_birth_days = (birthday - today).days
        
        html = parse_html(self.cfg['template_path'], [spawn_days, next_birth_days])
        print(html)
        return html
    
    