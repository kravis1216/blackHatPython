import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT)) # define listen IP address and port
    server.listen(5) # set the maximum number of connections
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=hanle_client, args=(client,))
        client_handler.start()

def hanle_client(client_socket):
    while client_socket:
        request = client_socket.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        client_socket.bind(b'ACK')

if __name__ == '__main__':
    main()
    