import socket


SIZE = 16
FORMAT = "utf-8"
PORT = 5000
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
conn, addr = server.accept()
msg = conn.recv(SIZE).decode()
print(msg)
conn.send((msg*2).encode())
conn.close()

