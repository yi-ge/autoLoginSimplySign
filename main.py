import schedule
import time

from task import task


schedule.every(3600).seconds.do(task)  # 每3600秒执行一次task函数

while True:
    schedule.run_pending()
    time.sleep(1)
