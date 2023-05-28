import zmq

host = "127.0.0.1"
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect(f"tcp://{host}:{port}")
sub.setsockopt(zmq.SUBSCRIBE, b"five")
while True:
    option, word_bytes = sub.recv_multipart()
    word = word_bytes.decode("utf-8")
    print("Subscribe: ", word)

# Subscribe:  Queen
# Subscribe:  flies
# Subscribe:  seize
# Subscribe:  gaily
# Subscribe:  great
# Subscribe:  swarm
# Subscribe:  trees
# Subscribe:  stand
# Subscribe:  queen
# Subscribe:  heard
# Subscribe:  great
# Subscribe:  Paris
# Subscribe:  youth
# Subscribe:  these
# Subscribe:  might
# Subscribe:  songs
# Subscribe:  glees
# Subscribe:  could
# Subscribe:  queen
# Subscribe:  We'rt
# Subscribe:  You'd
# Subscribe:  shade
# Subscribe:  Folks
# Subscribe:  would
# Subscribe:  think
# Subscribe:  About
# Subscribe:  crush