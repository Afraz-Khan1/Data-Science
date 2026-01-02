# making a program for arthimatic operations and tracking log messages using loggers.
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%Y - %m -%d %H - %M -%S',
    handlers=[ # you can also use manual filemode and filename but this is better handerls
        logging.FileHandler('app1.log'), # file for log messages
        logging.StreamHandler() # responsible for showing results here also
    ]
)
logger=logging.getLogger('Arthimatic_operation') # naming your logger so that in big programs you can identify from where the error produced.

def addition(a,b):
    result=a+b
    logger.debug(f" Addition of {a} + {b} = {result}")
    return result
def subtraction(a,b):
    result=a-b
    logger.debug(f"Subtraction of {a} - {b} = {result}")
    return result
def multiplication(a,b):
    result=a*b
    logger.debug(f"Multiplication of {a} * {b} = {result}")
    return result
def division(a,b):
    try:
       result=a/b
       logger.debug(f" Division of {a} / {b} = {result}")
       return result
    except ZeroDivisionError as e:
       logger.error("Zero division error:")
       print(e)
       return None

addition(5,7)
subtraction(3,4)
multiplication(12,2)
division(8,2)
division(8,0)


