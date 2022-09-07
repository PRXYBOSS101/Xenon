def encode(data, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(data,key)])

def decode(encoded, key):
    return encode(encoded, key)