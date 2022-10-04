import json

from .api import Api
from .logger import Logger


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
        results = [f'城市: {city}, 时间: {time}',
                   f'温度: {temperature}, 湿度: {humidity}',
                   f'风力: {wind_strength}, 风向: {wind_direction}']
        return results


class HeFengWeather(object):
    def __init__(self, cfg):
        self.cfg = cfg.weather_hefeng
        self.api = Api()
        self.logger = Logger(cfg, 'weather')
    
    def run(self):
        results1 = self._get_weather()
        results2 = self._get_air_index()
        results3 = self._get_weather_warn()
        return ['<h2>今日天气</h2>'] + results1 + results2 + results3 + ['\n']

    def _get_weather(self):
        resp = self.api.req('get_weather_hefeng', data=dict(
            key=self.cfg['key'],
            location=self.cfg['location']))
        res = json.loads(resp.text)['now']
        temperature = res['temp']
        type_ = res['text']
        wind_dir  = res['windDir']
        wind_scale = res['windScale']
        humidity = res['humidity']
        pressure = res['pressure']
        vis = res['vis']
        results = [f'<b>当前天气: {type_}</b>', 
                   f'气温: {temperature}℃, 湿度: {humidity}%',
                   f'风力: {wind_scale}级, 风向: {wind_dir}',
                   f'气压: {pressure}hpa, 能见度: {vis}km']
        return results

    def _get_air_index(self):
        resp = self.api.req('get_air_quality', data=dict(
            key=self.cfg['key'],
            location=self.cfg['location']))
        results = json.loads(resp.text)['daily']
        results = ['<b>{} {}</b> {}'.format(res['name'], res['level'], res['text']) for res in results]
        return results

    def _get_weather_warn(self):
        resp = self.api.req('get_weather_warn', data=dict(
            key=self.cfg['key'],
            location=self.cfg['location']))
        results = json.loads(resp.text)['warning']
        results = ['<b>{}</b> {}'.format(res['title'], res['text']) for res in results]
        return results
