import pyautogui

pyautogui.PAUSE = 2.5  # PyAutoGUI函数增加延迟为2.5秒：


def task():
    print("执行定时任务")
    # try:
    button_x, button_y = pyautogui.locateCenterOnScreen(
        '1.png', confidence=0.9, grayscale=True)
    pyautogui.click(button='right', x=button_x, y=button_y)
    # im1 = pyautogui.screenshot()
    # im1.save('my_screenshot.png')
    buttonLocation = pyautogui.locateOnScreen(
        '2.png', confidence=0.9, grayscale=True)
    pyautogui.click(buttonLocation[0] + 3, buttonLocation[1] + 3)

    pyautogui.write('Hello world!', interval=0.25)
    pyautogui.keyDown('enter')
    # except Exception as e:
    #     print(e)


task()
