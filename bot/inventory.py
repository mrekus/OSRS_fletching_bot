from utils import win32api
from utils import win32con
import time


def click_grapes_inventory(x=1457, y=357):
    win32api.SetCursorPos((x, y))
    time.sleep(0.49)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)


def click_jug_inventory(x=1458, y=394):
    win32api.SetCursorPos((x, y))
    time.sleep(0.51)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.12)
