import configparser
import logging
import sys
import string
from time import time
import csv

# taken from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
table = str.maketrans({key: None for key in string.punctuation})

class Timer:
    '''
    A time class that marks event times for a specific named period.
    Init to begin timing
    elapsed to get information
    '''
    def __init__(self, name):
        self.time = time()
        self.name = name

    def elapsed(self):
        print(f"Time for {self.name}: {round(time()-self.time, 3)}s")


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
