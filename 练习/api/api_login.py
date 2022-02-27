import requests

class ApiLogin():
    def api_post_login(self, url, mobile, code):
        headers = {"Content-Type": "application/json"}
        data = {"mobile": mobile, "code": code}
        return requests.post(url,headers=headers, json=data)