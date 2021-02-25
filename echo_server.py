"""An echo server that has a server thread and a client thread. ONLY 5 CONNECTIONS."""

import threading
import socket


def server() -> None:
    """A server thread that has a server thread"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8007
    host = 'localhost'
    server_socket.bind((host, port))
    server_socket.listen(1)

    for _ in range(5):
        conn, addr = server_socket.accept()
        data = conn.recv(100000000)
        print('connected: ', addr, data.decode('utf-8'))
        conn.send(data)
        conn.close()


def client() -> None:
    """A client thread that has a client thread"""
    for _ in range(5):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8007
        host = 'localhost'
        client_socket.connect((host, port))
        client_socket.send(input('> ').encode('utf-8'))
        data = client_socket.recv(100000000)
        print('received', data.decode('utf-8'), len(data), 'bytes')
        client_socket.close()


server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()
