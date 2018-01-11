# ** -- coding: utf-8 -- **
# !/usr/bin/env python
#
# Copyright (c) 2011 darkdarkfruit <darkdarkfruit@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

'''


'''

import json

STATUS_SUCCESSFUL = 'S'
STATUS_SUCCESSFUL_FULL_STRING = 'SUCCESSFUL'
STATUS_FAILED = 'F'
STATUS_FAILED_FULL_STRING = 'FAILED'

STATUSES = (STATUS_SUCCESSFUL, STATUS_FAILED)


class Message(dict):
    """
    (status is always in state: "S" or "F"(represents "Successful", "Failed"), no 3th state)

    |--------+--------+----------+----------+-------------------------------------------------------|
    | Field  | type   | Required | Optional | Meaning                                               |
    |--------+--------+----------+----------+-------------------------------------------------------|
    | status | string | * (S/F)  |          | Is the response successful?                           |
    | code   | any    |          | *        | CODE for application logic(Normally it is an integer) |
    | data   | any    |          | *        | Data(payload) of the response                         |
    | desc   | any    |          | *        | Description: normally it's a helping infomation       |
    | meta   | any    |          | *        | eg: servers/ips chain in distributed env.             |
    |        |        |          |          |                                                       |
    |--------+--------+----------+----------+-------------------------------------------------------|


    """

    def __init__(self, status):
        super(Message, self).__init__()
        self['status'] = status if status in STATUSES else STATUS_FAILED
        self['code'] = None
        self['data'] = None
        self['desc'] = None
        self['meta'] = None

    @property
    def status(self):
        """get status

        Arguments:
        - `self`:
        """
        return self['status']

    @status.setter
    def status(self, status):
        """get status

        Arguments:
        - `self`:
        """
        if status not in STATUSES:
            print(f'Invalid status: {status}. Nothing changes. Valid status are: {STATUSES}')
            return
        self['status'] = status

    @property
    def code(self):
        """get code

        Arguments:
        - `self`:
        """
        return self['code']

    @code.setter
    def code(self, code):
        """ set code

        Arguments:
        - 'self':
        - 'code' : set code
        """
        self['code'] = code

    @property
    def data(self):
        """get data

        Arguments:
        - `self`:
        """
        return self['data']

    @data.setter
    def data(self, data):
        """ set data

        Arguments:
        - 'self':
        - 'data' : set data
        """
        self['data'] = data

    @property
    def desc(self):
        """get desc

        Arguments:
        - `self`:
        """
        return self['desc']

    @desc.setter
    def desc(self, desc):
        """ set desc

        Arguments:
        - 'self':
        - 'desc' : set desc
        """
        self['desc'] = desc

    @property
    def meta(self):
        """get meta

        Arguments:
        - `self`:
        """
        return self['meta']

    @meta.setter
    def meta(self, meta):
        """ set meta

        Arguments:
        - 'self':
        - 'meta' : set meta
        """
        self['meta'] = meta

    def is_successful(self):
        return self.status == STATUS_SUCCESSFUL

    def is_failed(self):
        return self.status == STATUS_FAILED

    def mark_successful(self):
        self.status = STATUS_SUCCESSFUL

    def mark_failed(self):
        self.status = STATUS_FAILED

    def status_in_full_string(self):
        if self.status == STATUS_SUCCESSFUL:
            return STATUS_SUCCESSFUL_FULL_STRING
        elif self.status == STATUS_FAILED:
            return STATUS_FAILED_FULL_STRING
        else:
            print(f"Invalid status. Got {self.status}. But valids are: {STATUSES}")
            return ''

    def as_dict(self, skip_none=False):
        if skip_none:
            return {k: v for k, v in self.items() if v is not None}
        else:
            return {k: v for k, v in self.items()}

    def dumps(self, skip_none=False):
        return json.dumps(self.as_dict(skip_none=skip_none))

    # def __getattr__(self, name):
    #     try:
    #         return self[name]
    #     except KeyError as e:
    #         raise AttributeError(e)
    #
    # def __setattr__(self, name, value):
    #     self[name] = value

    @classmethod
    def load_from_dict(cls, d) -> 'Message or None':
        if 'status' not in d:
            msg = 'Could not found field:"status" in dict, returning None'
            print(msg)
            return None

        if d['status'] not in STATUSES:
            print(f'Invalid status. Got: {d["status"]}, but valid are: {STATUSES}')
            return None

        msg = cls(d['status'])
        for key in msg.keys():
            if key in d:
                msg[key] = d[key]
        return msg

    @classmethod
    def loads(cls, json_bytes):
        try:
            d = json.loads(json_bytes)
        except Exception as e:
            msg = 'Json could not load from bytes[:30]:"%s". Returning None. Exception: %s' % (json_bytes[:30], e)
            print(msg)
            return None

        return cls.load_from_dict(d)


class SuccessfulMessage(Message):
    def __init__(self):
        super(SuccessfulMessage, self).__init__(STATUS_SUCCESSFUL)


class FailedMessage(Message):
    def __init__(self):
        super(FailedMessage, self).__init__(STATUS_FAILED)


def make_successful_message(code=None, data=None, desc=None, meta=None):
    msg = Message(STATUS_SUCCESSFUL)
    msg.code = code
    msg.data = data
    msg.desc = desc
    msg.meta = meta
    return msg


def make_failed_message(code=None, data=None, desc=None, meta=None):
    msg = Message(STATUS_FAILED)
    msg.code = code
    msg.data = data
    msg.desc = desc
    msg.meta = meta
    return msg
