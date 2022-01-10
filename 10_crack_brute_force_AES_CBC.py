"""
Exercise:
Use Brute force to decrypt a message encrypted with AES-CBC,
Facts:
It was encrypted with a key that represents a phone number of someone from Tel-Aviv, padded with zeroes.

In other words :
9 digits, beginning with 036,
with trailing '0' to a length of 16 bytes,
like this: 036######0000000).
"""


import itertools
from Crypto.Cipher import AES
from Crypto import Random
from collections import Counter


plain_text = "The Times of London"
key = "0368679230000000"
# most frequent characters in English language
most_freq_eng = "etaion"
# Useful to remove punctuation and spaces
alphabet = "abcdefghijklmnopqrstuvwxyz"


def is_english(dec_text):
    counter = 0
    if dec_text.isascii():
        dec_text = dec_text.lower()
        freq_char = Counter(dec_text)
        freq_char = list(sorted(freq_char.items(), key=lambda x: x[1], reverse=True))
        for item in freq_char[:13]:
            if item[0] not in alphabet:
                freq_char.remove(item)
        for item in freq_char[:6]:
            if item[0] in most_freq_eng:
                counter += 1
        if counter >= 4:
            return dec_text





def encrypt(plain_text, key):
    key = bytes(key, "UTF-8")
    cipher = AES.new(key, AES.MODE_CBC)
    # When there is no padding, the block size must equal the cipher length
    # Padding is necessary for texts with length different from 16 bytes
    text_bytes = bytes(plain_text[:16], "UTF-8")
    enc_block = cipher.encrypt(text_bytes)
    return cipher.iv, enc_block


def decrypt(enc_text, iv):
    for val in itertools.count(0, 1):
        if val <= 999999:
            key = "036" + str(val).zfill(6) + "0000000"
            k = bytes(key, "UTF-8")
            cipher = AES.new(k, AES.MODE_CBC, iv)
            dec_text = cipher.decrypt(enc_text).decode("latin-1")
            output = is_english(dec_text)
            if output is not None:
                return output

    return "NOK"


if __name__ == "__main__":
    iv, enc_text = encrypt(plain_text, key)
    print(enc_text)

    dec_text = decrypt(enc_text, iv)
    print(dec_text)
    
