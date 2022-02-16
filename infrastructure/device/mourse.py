import pyautogui


class Mourse(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        self._tool = pyautogui
        pass

    def move_mourse(self, x, y, *args):
        self._tool.moveTo(x=x, y=y, *args)
        self._x = x
        self._y = y

    def left_click(self, x=None, y=None):
        self._tool.click(x=x, y=y)

    def double_left_click(self):
        self._tool.doubleClick()

    def right_click(self):
        self._tool.rightClick()

    def middle_click(self):
        self._tool.middleClick()

    def scroll(self, clicks):
        self._tool.scroll(clicks)
