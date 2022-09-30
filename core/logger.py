import logging
import os

from .utils import init_dir


class Logger(object):
    def __init__(self, cfg, name):
        cfg = cfg.log
        save_dir = cfg['save_dir']
        init_dir(save_dir, mode='append')
        
        self.logger = logging.getLogger(name)
        formatter = logging.Formatter(cfg['format'])
        file_handler = logging.FileHandler(os.path.join(save_dir, name + '.log'), 
                                           encoding='utf-8')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)        
        self.logger.setLevel(cfg['level'])

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)
    
    def warn(self, msg):
        self.logger.warn(msg)
    
    def error(self, msg):
        self.logger.error(msg)
