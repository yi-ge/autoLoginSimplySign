import pyautogui

from get_password import get_password

pyautogui.PAUSE = 2.5  # PyAutoGUI函数增加延迟为2.5秒：


def task():
    print("执行定时任务")
    try:
        button_x, button_y = pyautogui.locateCenterOnScreen(
            '1.png', confidence=0.9, grayscale=True)
        pyautogui.click(button='right', x=button_x, y=button_y)
        buttonLocation = pyautogui.locateOnScreen(
            '2.png', confidence=0.9, grayscale=True)
        pyautogui.click(buttonLocation[0] + 3, buttonLocation[1] + 3)

        pyautogui.write(get_password(), interval=0.25)
        pyautogui.keyDown('enter')
        print('执行成功')
    except Exception as e:
        print(e)
        print('执行异常或无需执行')


task()
