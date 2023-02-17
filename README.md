# api-auto
#### 接口自动化测试框架说明
- 本框架使用request+pytest+logging+allure搭建而成
- 框架主入口run.py文件
- pytest配置存放在pytest.ini文件中
- 框架支持接口关联和热加载方式
    - 接口关联格式：{{变量名称}}
    - 热加载格式: ${方法名(参数)}
- 测试用例格式
    ```
        "name":xxx, # 用例名称
        "requests":{}, # 请求信息
        "except":{
                "eq":{key:value} # 判断相等
                "contains": xxx  # 判断xxx在响应中存在
                },  # 用例断言信息 
        "extract":{}  # 需要提取的响应
    ```

##### 常用配置
- 项目host文件存放： config/config_host.yaml
- 日志配置字典存放:  config/LogDict.py
- 热加载方法存放: debug_talk.py

##### 用例配置
- 接口响应数据存放：extract.yaml
- 日志文件存放：log/
- 测试报告文件存放: reports/report
- 测试用例数据存放：data/*.json


