import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5059
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(SIZE)
conn, addr = server.accept()

msg = conn.recv(SIZE).decode()
msg = msg.strip('][').split(', ')

sum = 0
for i in msg:
    sum += 1
    print(i)

conn.send(str(sum).encode())
conn.close()



