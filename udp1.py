import socket

host = "192.168.1.120"
port = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

    s.bind((host, port))
    s.settimeout(5)
    data, addr = s.recvfrom(1024)
    print(f"received from {addr}\nobtained {data}")
    s.close()

except socket.timeout:
    print("Client didn't connect")
    s.close()
