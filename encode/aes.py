import base64
from Crypto.Cipher import AES
from Crypto import Random, pad, unpad



def encode(data, key):
    data = pad(data)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new( key, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( data ) ) 

def decode(data, key):
    data = base64.b64decode(data)
    iv = data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return unpad(cipher.decrypt( data[16:] ))