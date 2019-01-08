# coding: utf-8

import socket
import threading


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Connection de: %s %s" % (self.ip, self.port,))

    def run(self):
        try:
            while True:
                r = self.clientsocket.recv(2048).decode("utf-8")
                print("recu: " + r + " de: " + str(self.ip))
                self.clientsocket.send(b"bien envoye: " + bytes(r, "utf-8"))
        except:
            print("[-] Déconnection de: %s %s" % (self.ip, self.port,))


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 446))
print('En écoute...')

while True:
    tcpsock.listen(10)
    print("En attente de connexion...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
