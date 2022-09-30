import yagmail

from .logger import Logger
from .utils import parse_html


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
        content = parse_html(self.cfg['template_path'], [subject] + results)
        self.client.send(to, subject, content)
