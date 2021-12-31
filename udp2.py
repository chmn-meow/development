import socket

host = "192.168.1.120"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s.sendto("hello all".encode(), (host, port)))
s.close()
