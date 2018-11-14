from celery import Celery

app = Celery(__name__,broker='amqp://zy:123456@192.168.52.101',
             backend='redis://192.168.52.101:6379/0')

@app.task
def add(x, y):
    print('Listen...')
    return x + y