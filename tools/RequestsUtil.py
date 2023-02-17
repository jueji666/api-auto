import requests
import common.ExtraValueReplace  as evr
from tools.LoggerUtil import write_log


class RequestsUtil():
    session = requests.session()

    def __init__(self, bass_url):
        self.bass_url = bass_url

    # 统一发送请求方法
    def send_request(self,**kwargs):
        write_log("请求信息")
        # 组装接口url
        self.url = self.bass_url+kwargs["path"]
        write_log("url：{}".format(self.url))
        # 处理请求方式
        self.method = str(kwargs["method"]).lower()
        write_log("method：{}".format(self.method))
        kwargs.pop("path")
        kwargs.pop("method")

        # 处理传文件
        self.files = None
        if "files" in kwargs.keys():
            self.files = kwargs["files"]
            for key,value in self.files.items():
                self.files[key] = open(value, "rb")
                write_log("files:{}".format(self.files[key]))

            kwargs.pop("files")

        # 替换请求参数，并发送请求
        for key,value in kwargs.items():
            if key in ["params", "data", "json", "headers"]:
                value = evr.replace_value(value)
                value = evr.replace_load(value)
                kwargs[key] = value
                write_log("{}:{}".format(key,kwargs[key]))

        res = RequestsUtil.session.request(url=self.url, method=self.method, files=self.files, **kwargs )
        return res

if __name__ == '__main__':
    base_url = r"https://api-qyb.beta.wxb.com"
    path = r"/sub_user/saveRole"
    headers = {
        "content-type" : "application/json;charset=UTF-8",
        'Cookie': 'PHPSESSID=8kmi25i6e28jdu1ehvi0bqap0l;'}
    data = {
        "role_name": "{}".format(6)
        }
    res=RequestsUtil(base_url).send_request(path=path,method="post",headers=headers, data=data)
    print(res.json())
