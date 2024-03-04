import socket


SIZE = 16
FORMAT = "utf-8"
PORT = 5000
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
msg = "A"
client.send(msg.encode())
print(client.recv(SIZE).decode())
client.close()
