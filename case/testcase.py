import unittest
import tools.send_requests as send_request
import tools.getyaml as getyaml

class Testrequest(unittest.TestCase):
    host = ""
    @classmethod
    def setUpClass(cls):
        path = "./../../config/host.yaml"
        data = getyaml.getyaml(path)
        cls.host =data["企云宝"]["test"]

    def setUp(self) -> None:
        path = getyaml.getyaml()
        self.url = Testrequest.host+path
        print(self.url)
        self.modth = "post"
        self.headers = {
            "content - type": "application / json;charset = UTF - 8",
            "cookie": "PHPSESSID=3bbv7bfg8sl951j7j9flho31q1;"
        }
        self.data = {

        }
    def test1(self):

        print(Testrequest.host)


if __name__ == '__main__':
    unittest.main()
