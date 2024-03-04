import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5058
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Almafa"
client.sendto(msg.encode(), ADDR)

msg2, addr = client.recvfrom(SIZE)
print(msg2.decode())
