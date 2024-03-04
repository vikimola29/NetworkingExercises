import socket

SIZE = 16
FORMAT = "utf-8"
PORT = 5058
SERVER = "localhost"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

msg, addr = server.recvfrom(SIZE)
msg = msg.decode()

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

vowelNum = 0
for i in msg:
    for j in vowels:
        if i == j:
            vowelNum += 1
print(msg + " " + str(vowelNum))
server.sendto(str(vowelNum).encode(), addr)
