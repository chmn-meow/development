import socket

host = "192.168.1.120"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

while True:
    conn, addr = s.accept()
    print(addr, "Now Connected")
    message = "Thank you for connecting"
    conn.send(message.encode())
    conn.close()
