import zmq

host = "127.0.0.1"
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect(f"tcp://{host}:{port}")
sub.setsockopt(zmq.SUBSCRIBE, b"vowels")
while True:
    option, word_bytes = sub.recv_multipart()
    word = word_bytes.decode("utf-8")
    print("Subscribe: ", word)

# Subscribe:  of
# Subscribe:  at
# Subscribe:  ease
# Subscribe:  evening
# Subscribe:  All
# Subscribe:  admired
# Subscribe:  a
# Subscribe:  In
# Subscribe:  of
# Subscribe:  as
# Subscribe:  a
# Subscribe:  of
# Subscribe:  Or
# Subscribe:  as
# Subscribe:  upon
# Subscribe:  It
# Subscribe:  And
# Subscribe:  unrivalled
# Subscribe:  of
# Subscribe:  a
# Subscribe:  as
# Subscribe:  Intends
# Subscribe:  off
# Subscribe:  as
# Subscribe:  as
# Subscribe:  at
# Subscribe:  Of
# Subscribe:  of
# Subscribe:  of
# Subscribe:  And
# Subscribe:  or
# Subscribe:  o'
# Subscribe:  of
# Subscribe:  a
# Subscribe:  even
# Subscribe:  at
# Subscribe:  it
# Subscribe:  About
# Subscribe:  and