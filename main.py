from bot.get_from_bank import click_string_bank, click_bow_bank
from bot.inventory import click_bow_inventory, click_string_inventory
from bot.deposit_to_bank import click_bank, deposit_bows
import win32gui
import pyautogui
import time
from random import uniform


def getShell():
    thelist = []

    def findit(hwnd, ctx):
        if win32gui.GetWindowText(hwnd) == "RuneLite - Finex":  # check the title
            thelist.append(hwnd)

    win32gui.EnumWindows(findit, None)
    return thelist[0]


def main():
    app_id = getShell()
    while True:
        time.sleep(round(uniform(0.08, 0.12), 2))
        click_bow_bank()
        click_string_bank()
        win32gui.SetForegroundWindow(app_id)
        pyautogui.press("esc")
        time.sleep(round(uniform(0.08, 0.12), 2))
        click_bow_inventory()
        click_string_inventory()
        time.sleep(round(uniform(0.7, 0.8), 2))
        win32gui.SetForegroundWindow(app_id)
        pyautogui.press("space")
        time.sleep(round(uniform(17, 18), 2))
        click_bank()
        time.sleep(round(uniform(0.2, 0.3), 2))
        deposit_bows()
        time.sleep(round(uniform(0.08, 0.12), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
