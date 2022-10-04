import datetime
import numpy as np
from pmdarima import auto_arima


class TimeSeries(object):
    def __init__(self, cfg):
        self.cfg = cfg.time_series

    def run(self):
        template_path, topic, update = self.cfg['template_path'], self.cfg['topic'], self.cfg['update_url']
        results, last = self._load_txt()
        topic = f'<h2>{topic}</h2>'
        btn = f'<a href={update}>今日发生？点击这里</a>'
        if results is None:
            return [topic, '数据不足，无法预测', btn, '\n']

        model = auto_arima(results)
        pred = model.predict(1)[0]
        if self.cfg['mode'] == 'date':
            pred = last + datetime.timedelta(days=round(pred))
        results = [topic, f'下次发生时间: {pred}', btn, '\n']
        return results

    def _load_txt(self):
        mode = self.cfg['mode']
        with open(self.cfg['data_path']) as f:
            results = list(filter(lambda x: len(x) > 0, [x.strip() for x in f.readlines()]))
            if len(results) < 3:
                return None, None
        if mode == 'number':
            results = np.array([int(res) for res in results])
            return results, None
        elif mode == 'date':
            results = [datetime.date(*[int(x) for x in res.split('-')]) for res in results]
            deltas = np.array([(results[i + 1] - results[i]).days for i in range(len(results) - 1)])
            return deltas, results[-1]
