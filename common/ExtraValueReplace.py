import tools.YamlUtil as yu
import json
from debug_talk import DebugTalk
from tools.LoggerUtil import write_log


def replace_value(data, filepath ="./../extract.yaml"):
    """
    接口关联替换方法封装
    将{{变量}}替换成 对应的变量数据
    """
    try:
        #如果数据是字典格式，需要转换成字符串
        if data and isinstance(data, dict):
            str = json.dumps(data)
        else:
            str = data

        # 替换数据
        while "{{" in str:
            start_index = str.index("{{")
            end_index = str.index("}}")
            old_value = str[start_index:end_index+2]
            new_value = yu.Yamlutil(filepath).get_yaml()[old_value[2:-2]]
            str = str.replace(old_value, new_value)

        # 将替换好的数据 转换成 原格式
        if data and isinstance(data, dict):
            data = json.loads(str)
        else:
            data = str

        return data

    except Exception as f:
        write_log("接口关联替换方法报错, 报错信息:{}".format(f),"error")

def replace_load(data):
    """
    热加载方法封装
    将${方法(参数)}替换成 方法执行后的结果。
    """
    try:
        # 如果数据是字典格式，需要转换成字符串
        if data and isinstance(data, dict):
            str = json.dumps(data)
        else:
            str = data

        # 替换数据
        while "${" in str:
            start_index = str.index("${")
            end_index = str.index("}")
            old_value = str[start_index:end_index+1]
            func_name = old_value[2:old_value.index("(")]
            func_params = old_value[old_value.index("(")+1:old_value.index(")")].split(",")

            # 判断有无参数
            if func_params ==[""]:
                new_value = getattr(DebugTalk(), func_name)()
            else:
                new_value = getattr(DebugTalk(), func_name)(*func_params)
            str = str.replace(old_value, new_value)

        # 将替换好的数据 转换成 原格式
        if data and isinstance(data, dict):
            data = json.loads(str)
        else:
            data = str

        return data
    except Exception as f:
        write_log("热加载方法报错, 报错信息:{}".format(f),"error")




if __name__=="__main__":
    data1 = {"name":"{{name}}",
            "age":"{{age}}"}
    data2 = "my name is {{name}}, age is {{age}}"
    data3 = {"time":"${get_nowtime()}",
            "age":"{{age}}"}
    data4 = "now time is ${get_nowtime()}"
    print(replace_value(data1))
    print(replace_value(data2))
    print(replace_load(data3))
    print(replace_load(data4))