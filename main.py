import schedule
import time

from task import task

from dotenv import load_dotenv


load_dotenv()  # 加载 .env 文件
schedule.every(3600).seconds.do(task)  # 每3600秒执行一次task函数

while True:
    schedule.run_pending()
    time.sleep(1)
