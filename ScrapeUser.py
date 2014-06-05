#!/usr/bin/env python -tt

###########################################################
##                                                       ##
##   ScrapeUser.py                                       ##
##                                                       ##
##                Author: Michael Garber-Barron          ##
##                Author: Tony Fischetti                 ##
##                           mich.gar.bar@gmail.com      ##
##                           tony.fischetti@gmail.com    ##
##                                                       ##
###########################################################

"""
Scrapes all relevant content for one OKCupid user
"""

__authors__ = ['Micharl Garber-Barron', 'Tony Fischetti']
__version__ = '0.1'

import sys
import requests

from utils import debug, PROF_PRE, dump




def handle_this_user(okcusername, s):
    """
    Takes the username of a OKCupid member .....

    Args:
        a username
        a requests session object
    """
    debug("Going to scrape user {}".format(okcusername))
    get_about(okcusername, s)




def get_about(okcusername, s):
    """
    Gets about page...
    """
    okcusername = "swagyolo666"
    relevant_page = ''.join([PROF_PRE, okcusername])
    debug("get_about() called()")
    debug("Attempting to fetch page: {}".format(relevant_page))
    resp = s.get("{}".format(relevant_page))
    debug("Response was....\n\n{}".format(resp))
    if not resp.status_code == 200:
        err_mes = "Couldn't fetch page {}... non-200 ({})get request"
        die(err_mes.format(relevant_page, resp.status_code))


def get_photos(okcusername, s):
    """
    Gets photos page...
    """

def get_questions(okcusername, s):
    """
    Gets questions page...
    """

def get_personality(okcusername, s):
    """
    Gets personality page...
    """


#################################################
# going it its own separate vefirication module #
#################################################
#def verify_user....
# if the use doesn;t exist
# is the page exists 



def main():
    s = requests.Session()
    login_info = {'password': 'compaq1',
                  'username': 'millovely'}
    s.post('http://www.okcupid.com/login', params=login_info)
    handle_this_user("helpyhelp", s)

    



if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)

