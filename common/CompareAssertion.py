from tools.LoggerUtil import write_log
class Assertion():

    def compare_assertion(self,expect,actually):
        write_log("预期结果:{}".format(expect))
        write_log("实际结果:{}".format(actually))
        try:
            flag = 0
            if expect and isinstance(expect, dict):
                for key,value in expect.items():
                    if key == "eq":
                        for key,value in value.items():
                            if key in actually.keys():
                                if value != actually[key]:
                                    flag = flag+1
                                    write_log("{}与实际结果不等".format(key),"error")
                                    break
                            else:
                                write_log("{} 不存在".format(key),"error")
                                break

                    elif key == "contains":
                        if value in actually.keys():
                            pass
                        else:
                            flag = flag+1
                            write_log("{} 不存在".format(value), "error")
                    else:
                        print("不支持的断言方式")
                        break

            if flag == 0:
                return True
            else:
                raise Exception("断言失败")
        except Exception as f:
            write_log("比较断言方法报错,异常信息:{}".format(f),"error")

if __name__ == '__main__':
    pass