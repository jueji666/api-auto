import yaml

# 获取yaml文件的数据
def getyaml(path):
    with open(path, "r", encoding= "utf-8") as f :
        jsconfig = yaml.load(f, Loader= yaml.FullLoader)
    return jsconfig





if __name__ == '__main__':
    path = "./config/host.yaml"
    data = getyaml(path)
    print(data)