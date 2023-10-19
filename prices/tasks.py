from celery import Celery
app = Celery('tasks') #defining the app name to be used in our flag

@app.task # registering the task to the app
def add(x, y):
    return x+y