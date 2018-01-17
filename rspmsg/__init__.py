"""

Rspmsg specification::

    |--------+--------+-----------+-----------+------------+-------------------------------------------------------|
    | Field  | type   | Required? | Optional? | value      | Meaning                                               |
    |--------+--------+-----------+-----------+------------+-------------------------------------------------------|
    | status | string | *         |           | "S" or "F" | Is the response successful?                           |
    | code   | any    |           | *         |            | CODE for application logic(Normally it is an integer) |
    | data   | any    |           | *         |            | Data(payload) of the response                         |
    | desc   | any    |           | *         |            | Description: normally it's a helping infomation       |
    | meta   | any    |           | *         |            | Meta info. eg: servers/ips chain in distributed env.  |
    |        |        |           |           |            |                                                       |
    |--------+--------+-----------+-----------+------------+-------------------------------------------------------|

* Field:status is always in state: "S" or "F"(represents "Successful", "Failed"), no 3th state.

"""
from .rspmsg import Message, make_successful_message, make_failed_message, s, f, loads, dumps

__author__ = 'darkdarkfruit'

VERSION_TUPLE = (0, 6, 3)
VERSION_TUPLE_IN_STR = [str(i) for i in VERSION_TUPLE]


def get_version():
    return '.'.join(VERSION_TUPLE_IN_STR)


__version__ = get_version()

if __name__ == '__main__':
    print(__version__)
