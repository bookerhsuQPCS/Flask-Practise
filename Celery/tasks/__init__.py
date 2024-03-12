from celery import Celery
import time


# 這邊我把 Backend 跟 Broker 分開主要是為了讓我可以用 redis-cli 看 內容
# Backend 跟 Broker 也可以為同一個資料庫
celery_app = Celery(
    __name__,
    backend='redis://localhost:6379/0',
    broker='redis://localhost:6379/1',
)

# 如果跟 Celery 實體不在同一個位置的話就必須進行 import
celery_app.conf['imports'] = ('tasks.mail', )

# 如果跟 Celery 實體在同一個位置的話則不必


@celery_app.task
def add(a, b):
    time.sleep(5)
    return a + b
