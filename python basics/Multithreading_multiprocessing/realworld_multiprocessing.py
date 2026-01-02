import math
import sys
import multiprocessing
import time

# this function is used to increase the limit of number of digits convertible to string. as in console numbers are displayed as 
# strings in python version >3.11 default is 4300 digits convertable to strings from int to str in order to get displayed. As
# we take user input for example in int but still with input we need to typecast it in int as input function also get input in string. 
sys.set_int_max_str_digits(100000) # size applies per single integer in a list.


def operation(numbers):
 result=math.factorial(numbers)
 print(f"Result of {numbers} is {result}")

if __name__=="__main__":

    numbers=[1000, 700,4000,8000] 
    start=time.time()
    with multiprocessing.Pool() as pool:
      pool.map(operation,numbers)
    end=time.time()
    print(f"Net time: {end-start}")