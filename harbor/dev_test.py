import requests

HARBOR_BASIC_AUTH = {
    'api': 'https://harbor.liwy.ng/api/v2.0',
    'username': 'admin',
    'password': '123QWE**..',
}

def make_request(api):
    u = HARBOR_BASIC_AUTH['username']
    p = HARBOR_BASIC_AUTH['password']
    api = api
    resp = requests.get(api, auth=(u, p),verify=False)
    print(resp.status_code)

make_request('https://harbor.liwy.ng/api/v2.0/ping')