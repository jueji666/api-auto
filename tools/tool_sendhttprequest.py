import requests
import json

class SendHttpRequest():
    def __init__(self, URL, Method, HEADERS, DATA = None):
        self.res = self.send_request(URL, Method, HEADERS, DATA)

    def send_get(self, URL, HEADERS, DATA = None):
        res = requests.get(url=URL, headers=HEADERS, params=DATA).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii= False)

    def send_post(self, URL, HEADERS, DATA = None):
        if HEADERS["content-type"].__contains__("application/json"):
            res = requests.post(url=URL, headers=HEADERS, data=json.dumps(DATA)).json()
        else:
            res = requests.post(url=URL, headers=HEADERS, data=DATA).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii= False)

    def send_request(self, URL, Method, HEADERS, DATA = None):
        res = None
        if Method == "get" or Method == "GET":
            res = self.send_get(URL, HEADERS, DATA)
        else:
            res = self.send_post(URL, HEADERS,  DATA)
        return res

if __name__ == '__main__':
    url = r"https://api-qyb.beta.wxb.com/sub_user/saveRole"
    headers = {
        "content-type" : "application/json;charset=UTF-8",
        'Cookie': 'PHPSESSID=8kmi25i6e28jdu1ehvi0bqap0l; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1641264888,1641533987,1641781698,1642156058; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1642401921; RMU=2900405; RMT=efbc768a8aa84da5cac384b9fcde68f9'
    }
    data = {
        "role_name": "{}".format(6)
        }
    print(SendHttpRequest(url,"post",headers,data).res)