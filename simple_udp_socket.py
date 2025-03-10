'''
To get the results by running this prgram

1. Open another terminal and run the command
   nc -u -l -p 9997
2. Start this program
3. Sending characters from UDP listener in another terminal complete normally
'''
import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"AAABBBCCC",(target_host, target_port))

# receive data
data, address = client.recvfrom(4096)

print(data.decode('utf-8'))
print(address)

client.close()
