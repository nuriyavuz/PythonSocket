import socket

s=socket.socket()

s.connect(("192.168.1.31",15555))
s.close()
