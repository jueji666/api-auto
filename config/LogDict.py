import time

# 日志配置字典
logging_dict ={
    "version":1, # 默认配置  值为1
    "disable_existing_loggers":False,  # 默认配置
    # 日志格式
    "formatters":{
        "pro":{
            "format":"[%(asctime)s] [%(levelname)s] [%(filename)s][%(lineno)d]：%(message)s",
            "datefmt":"%Y:%m:%d %H:%M:%S"
              }
     },
    # 日志筛选器
    "filiters":{},
    # 日志格式器
    "handlers":{
        "console_debug_handler":{
            "level":"DEBUG",  #日志级别
            "class":"logging.StreamHandler", # 输出到终端
            "formatter":"pro" # 日志格式
        },
        "file_debug_handler":{
            "level":"DEBUG",  #日志级别
            "class":"logging.FileHandler", # 输出到文件
            "filename": r"log/log_{}.log".format(time.strftime("%Y%m%d_%H-%d-%S")), # 日志文件存放路径
            "encoding": "utf-8", # 日志文件编码
            "formatter":"pro" # 日志格式
        }
    },
    # 日志记录器
    "loggers":{
        "log":{
            "handlers":["console_debug_handler","file_debug_handler"], # 可指定多个handler
            "level" : "DEBUG",
            "propagate": False # 默认为True,向更高级的logger传递日志
        }
    }
}