#!/usr/bin/env python -tt

###########################################################
##                                                       ##
##   utils.py                                            ##
##                                                       ##
##                Author: Michael Garber-Barron          ##
##                Author: Tony Fischetti                 ##
##                           mich.gar.bar@gmail.com      ##
##                           tony.fischetti@gmail.com    ##
##                                                       ##
###########################################################

"""
This is a collection of utility functions to be available to
all modules in this project

This also holds config vars/constants to be shared
"""

__author__ = 'Tony Fischetti'
__version__ = '0.1'

import sys

DEBUG = True
DBG_FILE = sys.stdout
ERR_FILE = sys.stderr
DUMP_FILE = open("./dump/dump.txt", "a")

# common url prefixes
PROF_PRE = "http://www.okcupid.com/profile/"


def debug(message, stream=DBG_FILE):
    if DEBUG:
        print(message, file=stream)

def die(message, stream=ERR_FILE):
    print(message, file=stream)
    sys.exit(1)

def dump(message, stream=DUMP_FILE):
    print(message.encode('utf-8'), file=stream)
