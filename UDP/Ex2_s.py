import socket


SIZE = 16
FORMAT = "utf-8"
PORT = 5056
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

msg, addr = server.recvfrom(SIZE)
msg = msg.decode()
leng = str(len(msg))
print(leng)

server.sendto(leng.encode(), addr)

