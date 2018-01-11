from .rspmsg import Message, make_successful_message, make_failed_message, s, f

__author__ = 'darkdarkfruit'

VERSION_TUPLE = (0, 5, 0)
VERSION_TUPLE_IN_STR = [str(i) for i in VERSION_TUPLE]



def get_version():
    return '.'.join(VERSION_TUPLE_IN_STR)

__version__ = get_version()

if __name__ == '__main__':
    print(__version__)
