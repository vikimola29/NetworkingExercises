import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5059
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = '["a", "b", "c"]'

client.sendto(msg.encode(), ADDR)
reply, addr = client.recvfrom(SIZE)
print(reply.decode())