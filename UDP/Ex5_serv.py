import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5059
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

msg, addr = server.recvfrom(SIZE)
msg = msg.decode()
msg = msg.strip('][').split(', ')

sum = 0
for i in msg:
    sum += 1
    print(i)

server.sendto(str(sum).encode(), addr)
