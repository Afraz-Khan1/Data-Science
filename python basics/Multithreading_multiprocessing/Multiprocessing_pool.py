from concurrent.futures import ProcessPoolExecutor
import time

def square_number(numbers):
    time.sleep(1)
    return f"number {numbers*numbers}"

numbers=[1,2,3,56,47,21,23,5]

if __name__=="__main__":
   with ProcessPoolExecutor(max_workers=3) as executer: # more the workers faster the theads or processes completes.time.sleep() just makes each task “pause” for 1 second → shows how workers overlap: while one worker sleeps, others can keep working.
    results=executer.map(square_number,numbers)
    
    for result in results:
      print(result)

