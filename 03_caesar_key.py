alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 0
plain_text = "jerusalem"

def encrypt(plain_text, key):
    encrypted_word = list()
    for char in plain_text:
        idx = 0
        for idx in range(0, len(alphabet), 1):
            if char == alphabet[idx]:
                encrypted_word.append(alphabet[idx - key])
    return "".join(encrypted_word)


if __name__ == "__main__":
    encrypted_word = encrypt(plain_text, key)
    print(encrypted_word)
