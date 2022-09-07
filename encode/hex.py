import binascii

def encode(data):
    return binascii.hexlify(data)

def decode(data):
    return binascii.unhexlify(data)