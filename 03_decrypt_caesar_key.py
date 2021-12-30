alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        print(j, i, k)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    for idx in range(0, 26, 1):
        plaintext = decrypt(ciphertext, idx)
        print(plaintext, -idx)
    

if __name__ == "__main__":
    brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")