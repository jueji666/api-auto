import yaml

class ReadYaml():
    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        filepath = "../data/"+self.filename
        with open(filepath, "r", encoding="utf-8") as f:
            file =yaml.load(f, Loader = yaml.FullLoader)
        return file


if __name__ == '__main__':
    filename = "login.yaml"
    file = ReadYaml(filename).read_yaml()
    print(file)

