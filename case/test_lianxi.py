import pytest
import allure
import tools.JsonUtil as js
from common.RebuildCase import rebuild_case


class TestLianXi():
    @allure.story("练习使用的接口")
    @pytest.mark.parametrize("caseinfo",js.Jsonutil(r"data/qyb/qyb_lianxi.json").get_json())
    def test_lianxi(self,caseinfo):
        allure.dynamic.title(caseinfo["name"])
        rebuild_case(caseinfo)


if __name__ == '__main__':
    pytest.main(["-vs"])
