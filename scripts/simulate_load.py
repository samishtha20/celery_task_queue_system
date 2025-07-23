from celery_app.tasks import cpu_bound_task, io_bound_task, dummy_task
import time

# Submit a large number of heavy CPU-bound tasks to trigger HPA scaling
def robust_trigger():
    print("Submitting 200 heavy CPU-bound tasks...")
    for _ in range(200):
        cpu_bound_task.apply_async()
    print("Submitting 50 IO-bound tasks...")
    for _ in range(50):
        io_bound_task.apply_async()
    print("Submitting 20 dummy tasks...")
    for _ in range(20):
        dummy_task.apply_async()
    print("Robust load simulation complete.")

if __name__ == "__main__":
    robust_trigger()
