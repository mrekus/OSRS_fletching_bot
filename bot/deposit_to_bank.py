from utils import win32api
from utils import win32con
import time


def click_bank(x=1267, y=323):
    win32api.SetCursorPos((x, y))
    time.sleep(0.45)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)


def deposit_wine(x=1322, y=336):
    win32api.SetCursorPos((x, y))
    time.sleep(0.45)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)
