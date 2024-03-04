import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5059
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
conn, addr = server.accept()

msg = conn.recv(SIZE).decode()

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

vowelNum = 0
for i in msg:
    for j in vowels:
        if i == j:
            vowelNum += 1
print(msg + " " + str(vowelNum))

conn.send(str(vowelNum).encode())
conn.close()