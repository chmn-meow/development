import socket

host = "192.168.1.120"
port = 12345
server = socket.socket()
server.bind((host, port))
print("[+] Server Started")
print("[+] Listening for connection...")
server.listen(1)
client, client_addr = server.accept()
print(f"[+] {client_addr} Client connected to the server")

while True:
    command = input("Enter Command:\n> ")
    command = command.encode()
    client.send(command)
    print("[+] Command sent")
    output = client.recv(10214)
    output = output.decode()
    print(f"Output:\n> {output}")
