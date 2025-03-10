#check harbor health
from config import auth
import requests
import json

harbor_auth = auth.HARBOR_BASIC_AUTH

class ListProject():
    def __init__(self,auth):
        self.username = auth['username']
        self.password = auth['password']
        self.url = 'https://harbor.liwy.ng/api/v2.0/projects?page=1&page_size=40&with_detail=true'
        self.headers = {'Content-Type': 'application/json'}
    def list_project(self):

        resp = requests.get(self.url,auth=(self.username,self.password),headers=self.headers,timeout=5,verify=False)
        if resp.status_code != 200:
            print(resp.status_code)
        else:
            return resp.text


if __name__ == '__main__':
    list = ListProject(auth=harbor_auth)
    #print(check.check_health())
    resp = json.loads(list.list_project())
    print(type(resp))
    for project in resp:
        print(project)