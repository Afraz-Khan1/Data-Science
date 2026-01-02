# each process has its own memory management.
import multiprocessing
import time # just to record how much time it take to complete the task.

def square():
    for i in range(5):
        time.sleep(1.5)
        print(f"square: {i*i}")

def cube():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

if __name__=="__main__": # entry point it should be included or else p1 p2 creating and starting will run and import script in loop program hangs.
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)

#start process
    t1=time.time()
    p1.start()
    p2.start()

#wait for process to complete
    p1.join()
    p2.join()
    fin_time=time.time()-t1
    print(f"total time: {fin_time}")
#create processes
