from time import sleep
import pyautogui


def task():
    print("执行定时任务")
    button_x, button_y = pyautogui.locateCenterOnScreen('1.png')
    if button_x is not None:
        pyautogui.click(button='right', x=button_x, y=button_y)
        sleep(1)
        button_x, button_y = pyautogui.locateCenterOnScreen('2.png')
        pyautogui.click(button_x, button_y)


task()
