import socket

s = socket.socket()

print("scoket created")

s.bind(('localhost', 9000))

s.listen(5)
print("waiting for client")

while True:
    c, ipadd = s.accept() #client object, ip address port number
    print("connection essatablished with ", ipadd)
    c.send(bytes("HAR HAR MAHADEV", 'utf-8'))
    c.close()