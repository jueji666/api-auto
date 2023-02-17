import yaml
from tools.LoggerUtil import write_log

# yaml工具类
class Yamlutil():
    def __init__(self, filepath):
        self.filepath = filepath
    # 获取yaml文件数据
    def get_yaml(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                file = yaml.load(f, Loader=yaml.FullLoader)
            return file
        except Exception as f:
            write_log("get_yaml方法报错，异常信息：{}".format(f), "error")

    # 往yaml文件写入数据
    def write_yaml(self, data):
        try:
            with open(self.filepath, "a", encoding= "utf-8") as f:
                yaml.dump(data=data, stream=f, allow_unicode=True)
        except Exception as f:
            write_log("write_yaml方法报错，异常信息：{}".format(f), "error")
    # 清空yaml文件数据
    def clear_yaml(self):
        try:
            with open(self.filepath, "w", encoding= "utf-8") as f:
                f.truncate()
        except Exception as f:
            write_log("clear_yaml方法报错，异常信息：{}".format(f), "error")

if __name__ == "__main__":
    path = "../extract.yaml"
    data = {"name": "zhangsan",
            "age": 11}
    Yamlutil(path).write_yaml(data)
    print(Yamlutil(path).get_yaml())
    print(type(Yamlutil(path).get_yaml()))


