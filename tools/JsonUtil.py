import json
from tools.LoggerUtil import write_log

# 获取文件的数据
class Jsonutil():
    def __init__(self, filepath):
        self.filepath = filepath

    def get_json(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                file = json.load(f)
            return file
        except Exception as f:
            write_log("获取json文件数据方法报错，异常信息：{}".format(f),"error")

if __name__ == '__main__':
    path = r"../data/qyb/qyb_lianxi.json"
    data = Jsonutil(path).get_json()
    print(data)
