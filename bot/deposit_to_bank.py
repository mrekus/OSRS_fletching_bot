import win32api
import win32con
import time
from random import randint, uniform


def click_bank(x=randint(939, 1015), y=randint(293, 333)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))


def deposit_bows(x=randint(991, 1014), y=randint(324, 342)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
