import os
import logging
import pyautogui

from get_password import get_password

pyautogui.PAUSE = 2.5  # PyAutoGUI函数增加延迟为2.5秒：

# 设置当前执行目录为脚本所在目录
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# 配置日志记录
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def task():
    logging.info("执行定时任务")
    try:
        button_x, button_y = pyautogui.locateCenterOnScreen(
            '1.png', confidence=0.9, grayscale=True)
        pyautogui.click(button='right', x=button_x, y=button_y)
        buttonLocation = pyautogui.locateOnScreen(
            '2.png', confidence=0.9, grayscale=True)
        pyautogui.click(buttonLocation[0] + 3, buttonLocation[1] + 3)

        pyautogui.write(get_password(), interval=0.25)
        pyautogui.keyDown('enter')
        logging.info('执行成功')
    except Exception as e:
        logging.error("发生错误：{}".format(e))
        logging.info('执行异常或无需执行')


task()
