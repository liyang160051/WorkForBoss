import os.path
import time

import pyautogui
import os


class Browser(object):
    def __init__(self):
        self._tool = pyautogui

    def get_location_by_pic(self, imgPath):
        dir = os.path.dirname(__file__)
        dir = os.path.join(dir, os.pardir, os.pardir, os.pardir, "resource")
        imgPath = os.path.join(dir, imgPath)
        imgPath = os.path.abspath(imgPath)
        print(imgPath)
        coords = self._tool.locateOnScreen(imgPath, confidence=0.6)
        if coords is None:
            return None, None
        x, y = self._tool.center(coords)
        return x, y

    def screenshot(self, savePath):
        self._tool.screenshot(savePath)


if __name__ == '__main__':
    # x, y = Browser().get_location_by_pic("img/log_in_btn.png")
    # print(x, y)
    c = pyautogui.locateOnScreen("test.png", confidence=0.5)
    print(c)
