from Crypto.Cipher import AES
from Crypto import Random

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Morbi id nulla porta, sodales sapien ac, imperdiet nisi. \
Integer quam mi."


def aes_encrypt(plaintext, k):
    iv = Random.get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    # When there is no padding, the block size must equal the cipher length
    # Padding is necessary for texts with length different from 16 bytes
    b_string = plaintext[:16]
    cbytes = cipher.encrypt(bytes(b_string, "UTF-8"))
    return iv + cbytes
    # return iv + ciphertext (in bytes)

def aes_decrypt(ciphertext, k):
    # as iv has a length of 16 + is the first substring of the ciphertext:
    iv = ciphertext[:16]
    b_enc_text = ciphertext[16:]
    cipher = AES.new(k, AES.MODE_CBC, iv)
    return cipher.decrypt(b_enc_text).decode()


if __name__ == "__main__":
    plaintext = LOREM
    # Key has to be exchanged separately
    key = Random.get_random_bytes(16)
    enc_text = aes_encrypt(LOREM, key)
    print(enc_text)

    dec_text = aes_decrypt(enc_text, key)
    print(dec_text)


"""
Working solution for TAU exercise:
from Crypto.Cipher import AES
from Crypto import Random

def aes_encrypt(plaintext, k):
    iv = Random.get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    # When there is no padding, the block size must equal the cipher length
    # Padding is necessary for texts with length different from 16 bytes
    # no need to encode in bytes for the TAU exercise
    cbytes = cipher.encrypt(plaintext[:16])
    return iv + cbytes
    # return iv + ciphertext (in bytes)

def aes_decrypt(ciphertext, k):
    # as iv has a length of 16 + is the first substring of the ciphertext:
    iv = ciphertext[:16]
    b_enc_text = ciphertext[16:]
    cipher = AES.new(k, AES.MODE_CBC, iv)
    return cipher.decrypt(b_enc_text).decode()
"""