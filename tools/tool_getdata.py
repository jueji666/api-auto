from tools.tool_readfile import ReadFile

class GetData():
    def __init__(self, filepath):
        self.filepath = filepath

    def getyamldata(self):
        file = ReadFile(self.filepath).getyaml()
        arrs = []
        for data in file.values():
            arrs.append((data.get("name"),
                         data.get("path"),
                         data.get("method"),
                         data.get("headers"),
                         data.get("data"),
                         data.get("expect_result"),
                         data.get("expect_code")
                         ))
        return arrs

if __name__ == "__main__":
    filepath = "./../data/qyb/qyb_lianxi.yaml"
    a = GetData(filepath).getyamldata()
    print(a)

