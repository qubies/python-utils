import configparser
import logging
import sys
import string
from time import time
import csv
from functools import wraps

def print_banner(s, width=80, banner_token='-'):
    if len(s) > width:
        return s
    rem = width-len(s)
    rhs = rem//2
    lhs = rem-rhs
    if rhs > 0:
        rhs_pad = " " + (rhs-1)*banner_token
    else:
        rhs_pad = ""
    lhs_pad = (lhs-1)*banner_token + " "
    print(lhs_pad + s + rhs_pad, file=sys.stderr)


def print_banner_completion_wrapper(s, width=80, banner_token='-'):
    def wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print_banner(s, width, banner_token)
            result = func(*args, **kwargs)
            print_banner("Done " + s, width, banner_token)
            print(file=sys.stderr)
            return result
        return wrapper
    return wrap

sentencepiece_init = False

# taken from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
table = str.maketrans({key: None for key in string.punctuation})

class Timer:
    '''
    A time class that marks event times for a specific named period.
    Init to begin timing
    since_start to get time from init, also resets last
    '''
    def __init__(self, name):
        self.start = time()
        self.name = name
        self.__update__()

    def __update__(self):
        self.last=time()

    def since_start(self, reset_last=True):
        print(f"Time for {self.name}: {round(time()-self.start, 3)}s")
        if not reset_last: return
        self.__update__()
    
    def since_last(self):
        print(f"Time since last timer update for {self.name}: {round(time()-self.last, 3)}s")
        self.__update__()


def  start_logger(log_file, log_level=logging.DEBUG):
    '''
    Starts a common format logger
    '''
    logging.basicConfig(filename=log_file, level=log_level, format='%(levelname)s <--> %(asctime)s ->> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Logger Started")


def error_print(*args, **kwargs):
    '''
    Just prints to stderr
    '''
    print(*args, file=sys.stderr, **kwargs)


# load a configuration file
def load_config(file_name):
    '''
    brings in a config file as a dict
    '''
    config = configparser.ConfigParser()
    config.read(file_name)
    return config


# append a string to a file
def append_string_to_file(file_name, string):
    '''
    guess.... what... this... does
    '''
    with open(file_name, "a") as file:
        file.write(string)


def remove_punctuation(string):
    '''
    remove all punctuation from a string
    '''
    return string.translate(table)


def get_csv_rows(file_name, delimiter=','):
    '''
    get the number of rows in a csv
    '''
    return sum(1 for row in csv.reader( open(file_name)))


def read_csv(file_name, delimiter=','):
    '''
    reads in a csv as a dict so you can deal with it
    '''
    with open(file_name, mode='r') as csv_file:
        reader = csv.DictReader(tsv_file, delimiter=delimiter)
        for row in reader:
            yield (row, num_rows)

def word_tokenizer(sentence):
    global sentencepiece_init

    if not sentencepiece_init:
        sentencepiece_init = True
        global mysentencepiece
        import myutils.sentencepiece as mysentencepiece

    return mysentencepiece.to_tokens(sentence)


