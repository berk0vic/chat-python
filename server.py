import socket
import threading


#port and ips

ip = 'IP ADRESS'
port = 'PORT'
LISTENER_LIMIT = 5
#main
def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((ip, port))
    except:
        print(f"Unable to connect host {ip}:{port}")

    while True:

        client, adress = server.accept()
        print(f"Server succesfully conecting and starting...")
        print(f"Connected {adress[0]}:{adress[1]}")

if __name__ == '__main__':

    main()