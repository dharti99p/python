import threading
import datetime

print(datetime.datetime.now())
def task1():
    for i in range(5):
        print("Task 1 executing")

def task2():
    for i in range(5):
        print("Task 2 executing")

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
print(datetime.datetime.now())
print("All tasks completed")