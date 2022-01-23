"""
This is a copy of code provided by Nathan Jenning at https://realpython.com/python-sockets/
"""

import socket

HOST = "127.0.0.1"
PORT = 65432

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    main()