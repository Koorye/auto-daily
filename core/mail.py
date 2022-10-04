import yagmail

from .logger import Logger


class Mail(object):
    def __init__(self, cfg):
        self.cfg = cfg.mail
        self.logger = Logger(cfg, 'mail')
        self.client = yagmail.SMTP(host=self.cfg['host'],
                                   user=self.cfg['username'],
                                   password=self.cfg['password'])
    
    def run(self, results):
        to = self.cfg['to']
        subject = self.cfg['subject']
        self.client.send(to, subject, results)
