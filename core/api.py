import json
import requests


API = dict(
    get_weather=dict(
        url='http://www.weather.com.cn/data/sk/{1}.html',
        desc='中国天气网，根据城市代码获取天气',
        method='get'),
)

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "br, gzip, deflate",
    "Accept-Language": "zh-cn",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
}


class Api(object):
    def __init__(self):
        self.api = API
        self.headers = HEADERS
    
    def req(self, name, data=None, headers=None, fills=None):
        api = self.api.get(name)
        if api is None:
            print('api is not found!')
            return 
        url = api['url']
        method = api['method']
        
        if fills is not None:
            for idx, fill in enumerate(fills):
                url = url.replace('{' + str(idx + 1) + '}', fill)

        base_data = api.get('data', dict())
        if data is not None:
            base_data.update(data)
        base_headers = self.headers.copy()
        if headers is not None:
            base_headers.update(headers)
        
        if method == 'get':
            resp = requests.get(url, params=data, headers=headers)
        elif method == 'post':
            resp = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            raise NotImplementedError
        return resp
        