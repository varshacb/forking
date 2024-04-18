# echo-client.py

import socket

HOST = "127.0.0.1" 
PORT = 8000  
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cs.connect((HOST, PORT))
while True:
    msg = input("enter msg to be sent")
    cs.sendall(msg.encode())
    data = cs.recv(1024).decode()
    print(f"Received {data!r}")