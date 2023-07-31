import socket

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server.bind(('127.0.0.1', 31))

# Listen for incoming connections
server.listen()

print("Server started and is listening for connections...")

# Accept a connection
client_socket, addr = server.accept()

print(f"Connected with {addr}")

while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode('utf-8')
    print("Server successfully started..")
    if not message:
        break
    print(f"Received message: {message}")

    # Send a message to the client
    message = input("Enter your message: ")
    client_socket.send(message.encode('utf-8'))

server.close()
