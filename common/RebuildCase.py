import tools.YamlUtil as yaml
from common.CompareAssertion import Assertion
from tools.RequestsUtil import RequestsUtil
from tools.ExtractUtil import ExtractUtil

def rebuild_case(caseinfo):
    base_url = yaml.Yamlutil(r"config/config_host.yaml").get_yaml()["qyb"]["pro"]["api"]
    case_expect = caseinfo["expect"]
    res = RequestsUtil(base_url).send_request(**caseinfo["requests"])
    # 提取中间变量保存
    if "extract" in caseinfo.keys():
        ExtractUtil().extract_var(res, caseinfo["extract"])

    # 断言
    Assertion().compare_assertion(case_expect, res.json())
