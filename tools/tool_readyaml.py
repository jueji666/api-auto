import yaml

# 获取yaml文件的数据
class ReadYaml():
    def __init__(self, filepath):
        self.filepath = filepath

    def getyaml(self):
        with open(self.filepath, "r", encoding= "utf-8") as f :
            file = yaml.load(f, Loader= yaml.FullLoader)
        return file





if __name__ == '__main__':
    path = r"../config/config_host.yaml"
    # path = r"../config/config_host.yaml"
    data = ReadYaml(path).getyaml()
    print(data)