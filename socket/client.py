import socket

c = socket.socket()

c.connect(("localhost", 9000))

print(c.recv(1024).decode('utf-8'))

c.close()