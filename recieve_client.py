# -*- coding: utf-8 -*-
import socket

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.server_port = server_port
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        while True:
            try:
                recieved_string = self.connection.recv(4096)
                #print input_array
                if recieved_string != None:
                    print(str(recieved_string, "ascii"))
            except:
                print("connection closed.")
                self.connection.close()
                break

if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python recieve_client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client("37.187.53.31", 800)
    
