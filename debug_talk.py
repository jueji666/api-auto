import time
class DebugTalk():
    """
    存放需要动态执行的方法
    """

    def get_nowtime(self):
        return time.strftime("%Y:%m:%d %H:%M:%S")

if __name__ == '__main__':
    print(DebugTalk().get_nowtime())

