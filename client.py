import socket
import json
from encryption import encrypt_aes_gcm

# Use the same key as server (for testing)
key = b'Sixteen byte key for AES256--must be 32bytes!'[:32]

def client_program():
    host = socket.gethostname()
    port = 6000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower() != 'bye':
        encrypted_data = encrypt_aes_gcm(message, key)
        json_message = json.dumps(encrypted_data)
        client_socket.send(json_message.encode())

        # Receive plain text response
        data = client_socket.recv(4096).decode()
        print("Server says:", data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client_program()
