import tools.YamlUtil
import re
import jsonpath
from tools.LoggerUtil import write_log


class ExtractUtil():

    def extract_var(self,data, extract_data):
        """
        :param data: 原始数据
        :param extract_data: 需要提取的字段

        """
        try:
            for key,value in extract_data.items():
                # 正则提取
                if "(.+?)" in value or "(.*?)" in value:
                   result= re.match(value,data.text).group()
                   tempdata = {key: result}
                   tools.YamlUtil.Yamlutil("./../extract.yaml").write_yaml(tempdata)
                else:
                # json提取
                    result = jsonpath.jsonpath(data.json(),value)[0]
                    tempdata = {key: result}
                    tools.YamlUtil.Yamlutil("./../extract.yaml").write_yaml(tempdata)
        except Exception as f:
            write_log("extract_var方法报错，异常信息：{}".format(f),"error")

if __name__ == '__main__':
    pass