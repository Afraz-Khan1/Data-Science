import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
def print_letter():
    for i in "abcde":
        time.sleep(2)
        print(f"letter: {i}")

t1=threading.Thread(target=print_number) # while one thread is on sleep the other invoke and with respect to the timer. 
t2=threading.Thread(target=print_letter)

t=time.time()
#start the thread
t1.start()
t2.start()

# wait for the threads to complete
# the main thread is your program running if you dont use these line of code below the threads t1,t2 won't complete and main thread will continue before there completion.
t1.join()
t2.join()

finished_time=time.time()-t
print(f"total time: {finished_time}")