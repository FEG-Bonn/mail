import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 446))
while True:
    sleep(2)
    s.send(bytes(input("message: "), 'utf-8'))
    print(s.recv(2048).decode('utf-8'))
