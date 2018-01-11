#  What is it?

  A python rspmsg module with simplication and modification attached.


# Note:
  python version: >=3.6

  (For python2.7 version, use rspmsg_version < 0.9, eg: https://github.com/darkdarkfruit/rspmsg/releases/tag/v_0.7.1)


# Rspmsg specification


    ## Original rspmsg link:
    [https://labs.omniti.com/labs/rspmsg](https://labs.omniti.com/labs/rspmsg)


    ## What's modified:
    ### Fields:


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

## Decide essage type responded in server side

#### When do we set the message as successful or faild? It varies. Here are some suggestions.
* If the server can reponse with correspondent resource right now, we should mark the message as a 'S' (SUCCESSFUL) message.
* If the server can **NOT** response with correspondent resource right now, we should mark the message as a 'F' (FAILED) message while setting a meaningful code.
    * eg1:
    
            rspmsg_successful = {
                status : "S",
                ...
            }
    
    * eg2:

            # If we want to return a response message to tell client that:
            #   1. debug info: the message has flowed to nodes: ["192.168.1.6", "192.168.1.7"]
            #   2. Please wait 5 seconds to retry.
            # we might response a message like below:
            rspmsg_failed = {
                status : "F",
                code : 100,
                data : {
                    seconds: 5
                },
                desc : "Server is busy, please wait 5 seconds to continue",
                meta : {
                    nodes: ["192.168.1.6", "192.168.1.7"]
                }
    



# Install:
    * pip install rspmsg or (pip3 install rspmsg)
    Or
    * download the tarbal, decompress it, then run "python setup.py install"

# Test:
      # ensure you have the pytest for python3
      > pip3 install pytest
      > whereis pytest
      > pytest: /usr/local/bin/pytest
      > pytest --version
      > This is pytest version 3.3.2, imported from /usr/local/lib/python3.6/site-packages/pytest.py
      >
      > pytest rspmsg/

# API: (only 1 class and 2 functions)
  * class
  
        * Message
  * functions:

        * make_successful_message 
        * make_failed_message


#  Usage: (sample)

  
    Python 3.6.2 (default, Aug 10 2017, 10:07:10) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: import rspmsg
       ...: 
    
    In [2]: rspmsg.__version__
       ...: 
    Out[2]: '0.1.0'
    
    In [3]: msg = rspmsg.make_successful_message(code=0, data={'payload' : 'yes'})
       ...: 
    
    In [4]: msg
    Out[4]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [5]: msg.dumps()
    Out[5]: '{"status": "S", "code": 0, "data": {"payload": "yes"}, "desc": null, "meta": null}'
    
    In [6]: msg.dumps(skip_none=True)
    Out[6]: '{"status": "S", "code": 0, "data": {"payload": "yes"}}'
    
    In [7]: msg_failed = rspmsg.make_failed_message()
       ...: 
    
    In [8]: msg_failed
    Out[8]: {'code': None, 'data': None, 'desc': None, 'meta': None, 'status': 'F'}
    
    In [9]: msg_failed.dumps()
    Out[9]: '{"status": "F", "code": null, "data": null, "desc": null, "meta": null}'
    
    In [10]: msg_failed.dumps(skip_none=True)
    Out[10]: '{"status": "F"}'
    
    In [11]: msg_loaded = rspmsg.Message.loads(msg.dumps())
        ...: 
    
    In [12]: msg_loaded
    Out[12]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [13]: msg_loaded.data = 0
    
    In [14]: msg_loaded = rspmsg.Message.loads(msg.dumps())
        ...: 
    
    In [15]: msg_loaded
    Out[15]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [16]: msg_loaded.dumps()
    Out[16]: '{"status": "S", "code": 0, "data": {"payload": "yes"}, "desc": null, "meta": null}'
    
    In [17]: msg_loaded.dumps(skip_none=True)
    Out[17]: '{"status": "S", "code": 0, "data": {"payload": "yes"}}'
    
    In [18]: 
