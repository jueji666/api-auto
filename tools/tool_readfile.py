import yaml
import json

# 获取文件的数据
class ReadFile():
    def __init__(self, filepath):
        self.filepath = filepath

    def getyaml(self):
        with open(self.filepath, "r", encoding= "utf-8") as f:
            file = yaml.load(f, Loader= yaml.FullLoader)
        return file

    def getjson(self):
        with open(self.filepath, "r", encoding= "utf-8") as f:
            file = json.load(f)
        return file





if __name__ == '__main__':
    # path = r"../config/config_host.yaml"
    path = r"../data/qyb/qyb_lianxi.yaml"
    data = ReadFile(path).getyaml()
    print(data)