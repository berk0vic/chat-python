import socket
import threading




ip = 'IP ADRESS'
port = 'PORT'
LISTENER_LIMIT = 5

def main():

    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip, port))
    except:
        print(f"Unable to connect server {ip}:{port}")

if __name__ == '__main__':
    main()