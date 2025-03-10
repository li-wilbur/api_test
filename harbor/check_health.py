#check harbor health
from config import auth
import requests
import json

harbor_auth = auth.HARBOR_BASIC_AUTH

class CheckHealth:
    def __init__(self,auth):
        self.username = auth['username']
        self.password = auth['password']
        self.url = 'https://harbor.liwy.ng/api/v2.0/health'
        self.headers = {'Content-Type': 'application/json'}
    def check_health(self):

        resp = requests.get(self.url,auth=(self.username,self.password),headers=self.headers,timeout=5,verify=False)
        if resp.status_code != 200:
            print(resp.status_code)
        else:
            return resp.text


if __name__ == '__main__':
    check = CheckHealth(auth=harbor_auth)
    #print(check.check_health())
    resp = json.loads(check.check_health())
    resp = dict(resp)
    resp = resp['components']
    for d in resp:
        print(d)