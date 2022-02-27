from tools.read_yaml import ReadYaml
from parameterized import parameterized
def get_data(filename):
    # filename = "login.yaml"
    file = ReadYaml(filename).read_yaml()
    arrs = []
    for data in file.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")
                     ))
    print(arrs)
    return arrs
if __name__ == "__main__":
    get_data("login.yaml")
