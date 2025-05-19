import socket
import json
from encryption import decrypt_aes_gcm

# Use a shared key (should be securely exchanged in real applications)
key = b'Sixteen byte key for AES256--must be 32bytes!'[:32]

def server_program():
    host = socket.gethostname()
    port = 6000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print(f"Server listening on {host}:{port}...")

    conn, address = server_socket.accept()
    print("Connection from:", str(address))

    while True:
        data = conn.recv(4096).decode()
        if not data:
            break

        try:
            encrypted_data = json.loads(data)
            decrypted_message = decrypt_aes_gcm(encrypted_data, key)
            print("Decrypted from client:", decrypted_message)
        except Exception as e:
            print("Error decrypting message:", e)
            break

        # Send response
        response = input(" -> ")
        conn.send(response.encode())

    conn.close()

if __name__ == "__main__":
    server_program()
