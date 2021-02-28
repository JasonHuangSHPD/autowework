from requests import Session
import requests


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'wwf06a4f12f22063c3'
        self.corpsecret = '7B8FtCTSp0JHsZq1d_l2_tp78eLSVwqLAK4x9IBlJoY'
        self.s.params["access_token"] = self.get_token().get('access_token')

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # token = r.json().get('access_token')
        return r.json()
