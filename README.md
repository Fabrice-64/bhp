# BHP

## 01_tcp_connections
- 01 Multiple connections is a copy of Nathan Jennings tutorial at https://realpython.com/python-sockets/
** Don't forget to add the arguments for both the server and the client (host, port and for the client: number of connections)**
- 02 Echo connection is the bare bone of a connection.
- 03 Replace Linux Netcat with Python code
    ```$ python3 03_netcat.py --help```: displays the helper of netcat.py
    ```$ python3 03_netcat.py  -t 127.0.0.203 -p 5555 -l -c```: sets up a server listener
    ```python3 03_netcat.py -t 127.0.0.123  -p 5555``` : sets up a client
    Then hit keys  ctrl  D
    ```BHP: #> ```is displayed and type: ```ls -la``` to get access to current files
    Then hit again ctrl D and through ```>uname -a ``` you get the machine name


