"""
Implement a hash function simple_hash that given a string s,
computes its hash as follows:
it starts with r = 7, and for every character in the string,
multiplies r by 31,
adds that character to r,
and keeps everything modulo 2 power 16.
"""


from string import ascii_lowercase
import itertools

lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec id sem magna. Nunc fermentum nisl et justo ullamcorper luctus.
Phasellus metus magna, ornare at laoreet sit amet, rutrum efficitur dui.
Vivamus ut eleifend ante.
Phasellus sodales nec risus sit amet viverra.
Fusce id viverra lectus, eu rutrum ex. Suspendisse pulvinar. tttt
"""
power = pow(2, 16)


def simple_hash(s):
    r = 7
    for char in s:
        r = r * 31
        r = r + ord(char)
    return r % power


def simple_crack(hash, lorem):
    # with 2 ** 16 solutions, ascii_lowercase, repeat=5 is large enough.
    test_list = ["".join(item) for item in itertools.product(ascii_lowercase, repeat=5)]
    for item in test_list:
        output = simple_hash(item)
        if output == hash and item != lorem:
            return output, item


if __name__ == "__main__":
    lorem = lorem
    hash = simple_hash(lorem)
    print("Value lorem:", hash)

    output, item = simple_crack(hash, lorem)
    print(output, item)
