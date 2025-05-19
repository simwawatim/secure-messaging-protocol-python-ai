import socket


def server_program():

    # get the host
    host = socket.gethostname()
    port = 5000

    #bind the socket 
    server_socket = socket.socket()
    server_socket.bind((host, port))

    #configure the server
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:

        #receive data
        data = conn.recv(1024).decode()

        #close socket if data is not recieved
        if not data:
            break
        
        print("Connection fro user: " + str(data))
        data = input(' -> ')

        #send data to client
        conn.send(data.encode())

    #close the connection
    conn.close()
    
if __name__ == "__main__":
    server_program()

