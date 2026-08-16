from concurrent.futures import ThreadPoolExecutor
import time

def print_number(numbers):
    time.sleep(1)
    return f"number {numbers}"

numbers=[1,2,3,56,47,21,23,5]

with ThreadPoolExecutor(max_workers=3) as executer: # more the workers faster the theads or processes completes.time.sleep() just makes each task “pause” for 1 second → shows how workers overlap: while one worker sleeps, others can keep working.
    results=executer.map(print_number,numbers)

for result in results:
    print(result)