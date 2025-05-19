import socket


def client_program():
    #get the host name
    host = socket.gethostname()
    port = 5000

    #make connection

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().split() != 'bye':
        #send the message
        client_socket.send(message.encode())

        #recieve the message
        data = client_socket.recv(1023).decode()

        #display the message

        print("Recieved message from: " + data)

        #show prompt again
        message = input(" -> ")

    #close the socket
    client_socket.close()

if __name__ == '__main__':
    client_program()
