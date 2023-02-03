from bot.get_from_bank import click_grapes_bank, click_jug_bank
from bot.inventory import click_grapes_inventory, click_jug_inventory
from bot.deposit_to_bank import click_bank, deposit_wine
from utils import pyautogui
import time


def main():
    while True:
        time.sleep(1)
        click_grapes_bank()
        click_jug_bank()
        pyautogui.press("esc")
        click_grapes_inventory()
        click_jug_inventory()
        pyautogui.press("space")
        time.sleep(18)
        click_bank()
        deposit_wine()
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(5)
    main()
