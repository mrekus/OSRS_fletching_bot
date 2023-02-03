from bot.get_from_bank import click_grapes_bank, click_jug_bank
from utils import pyautogui
import time


def main():
    click_grapes_bank()
    click_jug_bank()
    pyautogui.press("esc")


if __name__ == "__main__":
    time.sleep(5)
    main()
