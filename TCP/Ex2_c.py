import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5057
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = "alabalaportocala"
client.send(msg.encode())

conn = client.recv(SIZE)
print(conn.decode())

client.close()