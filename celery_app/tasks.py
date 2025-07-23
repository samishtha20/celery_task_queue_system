from celery import Celery
import time

# Use localhost for broker if running load generator locally
app = Celery('tasks', broker='amqp://user:XfoJMqVgKg2tvG7I@localhost:5672//')

@app.task
def cpu_bound_task():
    # Increase workload to trigger higher CPU usage for HPA
    sum([i**2 for i in range(10**8)])

@app.task
def io_bound_task():
    time.sleep(5)

@app.task
def dummy_task():
    return "OK"
