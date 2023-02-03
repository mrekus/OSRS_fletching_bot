import win32api
import win32con
import time
from random import randint, uniform


def click_grapes_inventory(x=randint(1455, 1459), y=randint(355, 358)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))


def click_jug_inventory(x=1458, y=394):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.7, 0.8), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
