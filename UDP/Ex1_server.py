import socket


SIZE = 16
FORMAT = "utf-8"
PORT = 5055
SERVER = "localhost"
ADDR = (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

msg, addr = server.recvfrom(SIZE)
msg = msg.decode()
print(msg)
server.sendto((msg*2).encode(), addr)