import logging
logging.basicConfig(
    # in order to write these logs in file
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s -%(name)s - %(levelname)s -%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)
