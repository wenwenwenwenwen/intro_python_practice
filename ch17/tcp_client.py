import socket
from datetime import datetime

address = ("localhost", 6789)
max_size = 1000

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b"Hey!")
data = client.recv(max_size)
print("At", datetime.now(), "someone replied", data)
client.close()

# Starting the client at 2023-05-28 15:22:55.208505
# At 2023-05-28 15:22:55.209507 someone replied b'Are you talking to me?'