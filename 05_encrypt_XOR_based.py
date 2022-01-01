import random
import string
my_text = '1234567890'
key = 'aaaaaaaaaa'
random_list = list()
bin_keys = list()


def create_bin_keys():
    bin_keys = [format(ord(item), '08b') for item in key]
    return bin_keys


def encode_to_bin(text):
    bin_list = [format(ord(item), '08b') for item in text]
    return bin_list


def encrypt_XOR(bin_list, bin_keys):
    enc_list = list()
    fitted_bin_keys = bin_keys[:len(bin_list)]
    for idx in range(len(bin_list)):
        enc_char = int(bin_list[idx], 2) ^ int(fitted_bin_keys[idx], 2)
        enc_list.append(format(enc_char, '08b'))
    return enc_list


def convert_encrypt_to_char(enc_list):
    return "".join([chr(int(item, 2)) for item in enc_list])


def decrypt(enc_list, bin_keys):
    dec_list = list()
    for idx in range(len(enc_list)):
        dec_char = int(enc_list[idx], 2) ^ int(bin_keys[idx], 2)
        dec_list.append(format(dec_char, '08b'))
    return "".join([chr(int(item, 2)) for item in dec_list])


if __name__ == "__main__":
    print("Before encryption: ", my_text)
    bin_list = encode_to_bin(my_text)
    print("String in Binary: ", bin_list)
    bin_keys = create_bin_keys()
    print("Binary keys: ", bin_keys[:len(bin_list)])
    enc_list = encrypt_XOR(bin_list, bin_keys)
    print("Encrypted String: ", enc_list)
    conv_string = convert_encrypt_to_char(enc_list)
    print(conv_string)
    result = decrypt(enc_list, bin_keys)
    print("Decrypted String: ", result)

