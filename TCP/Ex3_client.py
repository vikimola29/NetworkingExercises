import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5059
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = "Almafacska"
client.send(msg.encode())

reply = client.recv(SIZE).decode()
print(reply)
