import os
from infrastructure.device.keyboard import KeyBoard
from infrastructure.device.mourse import Mourse
from infrastructure.device.browser.chrome import Chrome


class Boss(object):

    def __init__(self, alias):
        self._alias = alias
        self._keyBoard = KeyBoard()
        self._mourse = Mourse()
        self._browser = Chrome()
        pass

    def _execute_cmd(self, cmd):
        result = os.system(cmd)
        return True if 0 == result else False

    def open_browser(self, baseUrl="https://www.zhipin.com/xian/"):
        cmd = "start chrome {url}".format(url=baseUrl)
        self._execute_cmd(cmd)

    def log_in(self):
        x, y = self._browser.get_location_by_pic("img/log_in_btn.png")
        print("find login btn is {x}, {y}".format(x=str(x), y=str(y)))
        if x is None or y is None:
            raise Exception("can not find login btn")
        self._mourse.move_mourse(x, y)
        self._mourse.left_click(x, y)

    def recommend_btn(self):
        x, y = self._browser.get_location_by_pic("img/recommend_btn.png")
        print("find recommend btn is {x}, {y}".format(x=str(x), y=str(y)))
        if x is None or y is None:
            raise Exception("can not find recommend btn")
        self._mourse.move_mourse(x, y)
        self._mourse.left_click(x, y)

    def _log_in_success(self):
        x, y = self._browser.get_location_by_pic("img/log_in_success.png")
        if x is not None and y is not None:
            print("login success")
            return True
        return False






