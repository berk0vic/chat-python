import socket

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 12345))

while True:
    # Send a message to the server
    message = input("Enter your message: ")
    client.send(message.encode('utf-8'))

    # Receive a message from the server
    message = client.recv(1024).decode('utf-8')
    print(f"Received message: {message}")

# Close the connection
client.close()
