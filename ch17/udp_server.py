from datetime import datetime
import socket

server_address = ("localhost", 6789)
max_size = 4096

print("Starting the server at", datetime.now())
print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

print("At", datetime.now(), client, "said", data)
server.sendto(b"Are you talking to me?", client)
server.close()

# Starting the server at 2023-05-28 15:07:47.373871
# Waiting for a client to call.
# At 2023-05-28 15:08:09.720342 ('127.0.0.1', 54290) said b'Hey!'