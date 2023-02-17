import logging
import logging.config
from config.LogDict import logging_dict

class LoggerUtil():

    def create_log(self):
        logging.config.dictConfig(logging_dict)
        log = logging.getLogger("log")
        return log

def write_log(log_message,level="info"):
    if level.lower()=="debug":
        LoggerUtil().create_log().debug(log_message)
    elif level.lower()=="info":
        LoggerUtil().create_log().info(log_message)
    elif level.lower()=="warring":
        LoggerUtil().create_log().warning(log_message)
    elif level.lower()=="error":
        LoggerUtil().create_log().error(log_message)
        raise Exception("log_message")
    else:
        print("日志级别错误")


if __name__ == '__main__':
    write_log("第一条日志")
    write_log("第二条日志")
