import win32api
import win32con
import time
from random import randint, uniform


def click_bank(x=randint(1264, 1269), y=randint(321, 324)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))


def deposit_wine(x=randint(1320, 1324), y=randint(334, 337)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.7, 0.8), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
