import asyncio
import socket

HOST = '127.0.0.1'
PORT = 8080

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print('Connected to the server!')

    client.send(b'Hello, from sync client!')

    response = client.recv(1024)
    print(f"Server response: {response.decode()}")
    client.close()
    print('Client closed!')


if __name__ == '__main__':
    main()