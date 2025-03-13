import requests
# 定义一个基础的 Harbor API 类，用于封装通用的请求逻辑
class HarborAPIClient:
    def __init__(self, auth):
        self.username = auth['username']
        self.password = auth['password']
        self.api = auth['api']
        self.headers = {'Content-Type': 'application/json'}

    def ping(self):
        url = self.api + '/ping'
        resp = self.make_request(url)
        if resp:
            result = resp.text
            return result == 'Pong'
        return False

    def make_request(self, url):
        try:
            # 发送 GET 请求
            resp = requests.get(url, auth=(self.username, self.password), headers=self.headers, timeout=5, verify=False)
            # 检查响应状态码
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            # 处理请求异常
            print(f"Request error: {e}")
            return None
    def list_projects(self):
        url = self.api + '/projects?page=1&page_size=40&with_detail=true'
        resp = self.make_request(url)
        return resp
    def check_health(self):
        url = self.api + '/health'
        resp = self.make_request(url)
        return resp