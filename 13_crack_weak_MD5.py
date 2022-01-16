"""
The function weak_md5 is a "weaker" version of MD5,
using only the first 5 bytes of the MD5 hash.
This means its hashing size is n=40 and it can be brute forced rather easily.

Implement a function find_collisions that loops over all the possible strings
until it finds an arbitrary collision
- that is, two different strings whose hash is the same -
and returns them (as a tuple).
"""

import base64
import hashlib
from itertools import product
from string import ascii_lowercase

my_string = "This is a secret key"


def weak_md5(s):
    s = bytes(s, "UTF-8")
    return hashlib.md5(s).digest()[:5].hex()


def find_collisions():
    test_list = ["".join(item) for item in product(ascii_lowercase, repeat=5)]
    cache = {}
    for item in test_list:
        h_pwd = weak_md5(item)
        if cache.get(h_pwd) and cache.get(h_pwd) != item:
            return h_pwd, item, cache.get(h_pwd), test_list.index(item)
        else:
            cache[h_pwd] = item


if __name__ == "__main__":

    h_pwd, rec_string, new_string, list_index = find_collisions()
    print(f" Pwd Collide at password : {h_pwd} with passwords {rec_string} and {new_string} at index {list_index}")
