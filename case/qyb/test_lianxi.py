import unittest
from parameterized import parameterized
from tools.tool_readyaml import ReadYaml
from tools.tool_getdata import GetData
from tools.tool_sendhttprequest import SendHttpRequest

class Test_lianxi(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     hostpath = r"../../config/config_host.yaml"
    #     cls.host = ReadYaml(hostpath).getyaml()["qyb"]["test"]
    #     cls.datapath = "../../data/qyb/qyb_lianxi.yaml"

    # @parameterized.expand(GetData(r"../../data/qyb/qyb_lianxi.yaml").getyamldata())
    def test01(self):
        hostpath = "../../config/config_host.yaml"
        self.host = ReadYaml(hostpath).getyaml()["qyb"]["test"]
        datapath = "../../data/qyb/qyb_lianxi.yaml"
        self.url = self.host+ReadYaml(datapath).getyaml()["001"]["path"]
        self.method = ReadYaml(datapath).getyaml()["001"]["method"]
        self.headers = ReadYaml(datapath).getyaml()["001"]["headers"]
        self.data = ReadYaml(datapath).getyaml()["001"]["data"]
        self.expect_result = ReadYaml(datapath).getyaml()["001"]["expect_result"]
        self.expect_code = ReadYaml(datapath).getyaml()["001"]["expect_code"]
        # r = SendHttpRequest(self.url,self.method,self.headers,self.data).res
        print(self.data)
        print(type(self.data))
