import socket

target_host = '127.0.0.1'
target_port = 9998

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to seerver
client.connect((target_host, target_port))

# send data
# client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
client.send(b"Hello")

# receive data
response = client.recv(4096)

print(response.decode())
client.close()
