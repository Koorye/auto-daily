import json

from .api import Api
from .logger import Logger
from .utils import parse_html


class Weather(object):
    def __init__(self, cfg):
        self.cfg = cfg.weather
        self.api = Api()
        self.logger = Logger(cfg, 'weather')
        
    def run(self):
        self.logger.info('Get weather from api...')
        resp = self.api.req('get_weather', fills=[self.cfg['sk']])
        res = resp.content.decode('utf-8')
        res = json.loads(res)['weatherinfo']
        city = res['city']
        time = res['time']
        temperature = res['temp']
        humidity = res['SD']
        wind_direction = res['WD']
        wind_strength = res['WS']
        html = parse_html(self.cfg['template_path'], [city, time, temperature, humidity, 
                                                      wind_direction, wind_strength])
        self.logger.info(f'Weather: \n{html}')
        return html
