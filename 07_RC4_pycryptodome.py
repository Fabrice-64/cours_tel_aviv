"""
The source of this code can be found at :https://github.com/nemozqqz/pycrypto-sample/blob/master/RC4.py
This is a Python3 adapted version.
"""
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto import Random

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Morbi id nulla porta, sodales sapien ac, imperdiet nisi. \
Integer quam mi."


def key_creation(key):
    return SHA256.new(key).digest()


def encrypt_msg(key, p):
    return ARC4.new(key).encrypt(p)


def decrypt_msg(key, msg):
    return ARC4.new(key).decrypt(msg).decode("UTF-8")


if __name__ == '__main__':
    key = bytes('This is a secret key', "UTF-8")
    plain_text = bytes(LOREM, "UTF-8")
    key = key_creation(key)
    print(key)
    enc_msg = encrypt_msg(key, plain_text)
    print(enc_msg)
    dec_msg = decrypt_msg(key, enc_msg)
    print(dec_msg)
