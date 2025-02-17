#!/usr/bin/python3
"""
    @Last update: MM/DD/YYYY
    @Version : 1.0
    @Author: Mohand TOUAHRI
    @Changelog:
    Date       | Ver   | Names            | Comments
    -----------|-------|------------------|---------------------------------------
    06/12/2023 | 1.0   | Mohand TOUAHRI   | Creation
"""

import argparse
import logging

#####################

OK       = 0
WARNING  = 1
CRITICAL = 2
UNKNOWN  = 3

#####################


def main():
    """ Main plugin logic goes here """

    ## Parse command-line arguments
    args = get_args()

    ## Uncomment to test logging levels against verbosity settings
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')
    # logging.fatal('fatal message')

    gtfo(OK)


def get_args():
    """ Supports the command-line arguments listed below. """

    parser = argparse.ArgumentParser(description="Your description")
    parser._positionals.title = "Arguments"
    parser._optionals.title   = "Options"
    parser.add_argument('-v', help='[-v|vv|vvv] Set verbosity level', action='count', default=0, dest='v')

    # CLI Argument 
    # parser.add_argument('arg', help='positionnal argument here')
    parser.add_argument('-x', '--extra', help='Your option here',default=None)
    parser.add_argument('-f', '--force', required=False, help='set force to True', action='store_true')
    ##############

    args = parser.parse_args()

    logging.getLogger().setLevel([logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG][args.v])
    logging.debug('Parsed arguments: {0}'.format(args))

    return args


def gtfo(exitcode, message=None):
    """ Exit gracefully with exitcode and (optional) message """

    logging.debug('Exiting with status {0}. Message: {1}'.format(exitcode, message))
    
    if message:
        print(message)
    exit(exitcode)


if __name__ == '__main__':
    ## Initialize logging before hitting main, in case we need extra debuggability
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(funcName)s] - %(levelname)s - %(message)s')
    main()
