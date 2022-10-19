from .api import Api


class YouthStudy(object):
    def __init__(self, cfg):
        self.cfg = cfg.youth_study
        self.api = Api()
    
    def run(self):
        headers = dict(token=self.cfg['token'])
        data = self.api.req('youth_study_history', headers=headers, mode='json').json()['data'][0]
        data = self.api.req('youth_study_org', data=data, headers=headers, mode='param').json()['data']
        msg = self.api.req('youth_study_commit', data=data, headers=headers, mode='json').json()['msg']
        return ['<h2>青年大学习</h2>' + msg + '\n']
