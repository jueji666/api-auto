import unittest
from parameterized import parameterized
# from tools.get_data import get_data
from tools.read_yaml import ReadYaml
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

class TestParam(unittest.TestCase):
    @parameterized.expand(get_data("login.yaml"))
    def test_a(self, url, mobile, code, expect_result, status_code):
        print(url, mobile, code, expect_result, status_code)
