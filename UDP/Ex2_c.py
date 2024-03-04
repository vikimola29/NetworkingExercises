import socket


SIZE = 16
FORMAT = "utf-8"
PORT = 5056
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "alabalaportocala"
client.sendto(msg.encode(), ADDR)

reply, addr = client.recvfrom(SIZE)
print(reply.decode())