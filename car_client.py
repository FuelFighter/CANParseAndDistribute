# -*- coding: utf-8 -*-
import socket
import timerHandler as th

class Client:
    """
    This is the chat client class
    """
    connected = True
    def __init__(self, host, server_port):
        
        self.timer = th.timer(10)
        self.timer.start()
        self.host = host
        self.server_port = server_port
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.host, self.server_port))
            self.connected = True
            print('Connected with server')
        except: 
            print('Could not connect to server')
            self.connected = False
            pass

    def reconnect(self):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.host, self.server_port))
            self.connected = True
            print('Reconnected with server')
        except: 
            print('Could not connect to server')
            self.connected = False
            pass

    def send(self, data):
        if self.timer.timeout():
            self.close()
            self.reconnect()
            self.timer.start()

        if self.connected:
            try:
                self.connection.sendall(bytes(data, "ascii"))
            except:
                self.close()
    def receive(self):
        if self.timer.timeout():
            self.close()
            self.reconnect()
            self.timer.start()
            
        try:
            data = self.connection.recv(1024)
            return data.decode('ascii')
        except:
            return ''
                
    def close(self):
        self.connected = False
        self.connection.close()
