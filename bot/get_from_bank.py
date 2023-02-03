from utils import win32api
from utils import win32con
import time


def click_grapes_bank(x=968, y=120):
    win32api.SetCursorPos((x, y))
    time.sleep(0.47)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.09)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.12)


def click_jug_bank(x=1016, y=120):
    win32api.SetCursorPos((x, y))
    time.sleep(0.53)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)
