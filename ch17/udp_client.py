from datetime import datetime
import socket

server_address = ("localhost", 6789)
max_size = 4096

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hey!", server_address)
data, server = client.recvfrom(max_size)
print("At", datetime.now(), server, "said", data)
client.close()

# Starting the client at 2023-05-28 15:08:09.719770
# At 2023-05-28 15:08:09.720514 ('127.0.0.1', 6789) said b'Are you talking to me?'