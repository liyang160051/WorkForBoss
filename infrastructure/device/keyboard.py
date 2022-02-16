import pyautogui


class KeyBoard(object):

    def __init__(self):
        self._tool = pyautogui
        pass

    def type_write(self, content):
        self._tool.typewrite(message=content, interval=0.5)

    def key_down(self, key):
        self._tool.keyDown(key)

    def key_up(self, key):
        self._tool.keyUp(key)
