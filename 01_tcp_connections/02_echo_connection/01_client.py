"""
This is a copy of code provided by Nathan Jenning at https://realpython.com/python-sockets/
"""

import socket


HOST = "127.0.0.1"
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, World!")
        data = s.recv(1024)

        print(f"Received: {data}")


if __name__ == "__main__":
    main()