from datetime import datetime
import socket

address = ("localhost", 6789)
max_size = 1000

print("Starting the server at", datetime.now())
print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5) # 最多讓5個client連結

client, addr = server.accept()
data = client.recv(max_size)

print("At", datetime.now(), client, "said", data)
client.sendall(b"Are you talking to me?")
client.close()
server.close()

# Starting the server at 2023-05-28 15:22:44.445150
# Waiting for a client to call.
# At 2023-05-28 15:22:55.209310 <socket.socket fd=4, family=AddressFamily.AF_INET,
# type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 6789), raddr=('127.0.0.1', 51668)> said b'Hey!'