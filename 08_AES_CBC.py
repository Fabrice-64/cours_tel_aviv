import json
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Morbi id nulla porta, sodales sapien ac, imperdiet nisi. \
Integer quam mi."


def encrypt_key(key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher


def aes_encrypt(plain_text, cipher):
    b_text = bytes(plain_text, "UTF-8")
    ct_bytes = cipher.encrypt(pad(b_text, AES.block_size))
    iv = b64encode(cipher.iv).decode("UTF-8")
    ciphertext = b64encode(ct_bytes).decode("UTF-8")
    result = json.dumps({'iv': iv, 'ciphertext': ciphertext})
    return result


def aes_decrypt(enc_iv_text, key):
    try:
        b64 = json.loads(enc_iv_text)
        iv = b64decode(b64['iv'])
        cipher_text = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size).decode("UTF-8")
        return plain_text

    except (ValueError, KeyError):
        print("Incorrect Decryption")


if __name__ == "__main__":
    plain_text = LOREM
    # Generate a 16 byte Key
    key = get_random_bytes(16)
    print(f"Key: {key}, it has to be securely forwarded to the receiver")
    cipher = encrypt_key(key)
    enc_iv_text = aes_encrypt(plain_text, cipher)
    print(f"Encrypted text: {enc_iv_text}.\
        It includes the initialization vector and the encrypted text")
    # Key is to be shared separately (and securely)
    dec_text = aes_decrypt(enc_iv_text, key)
    print(f" And Finally the decrypted text : {dec_text}")
