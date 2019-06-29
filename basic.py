import urllib
import time
import json


class Basic(object):
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        app_id = "wx19b4f75c757efea2"
        app_secret = "43521f75743dd679a5b477e6450bc581"
        post_url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'
        url_resp = urllib.urlopen(post_url)
        url_resp = json.loads(url_resp.read())
        self.__accessToken = url_resp['access_token']
        self.__leftTime = url_resp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
            return self.__accessToken

    def run(self):
        while True:
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()
