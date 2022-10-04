import datetime


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
        
        results = ['<h2>日历</h2>', 
                   f'今天是你出生的第<b>{spawn_days}</b>天，距离下次生日还有<b>{next_birth_days}</b>天',
                   '\n']
        return results
    