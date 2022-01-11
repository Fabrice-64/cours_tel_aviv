import hashlib


lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Nam quis tristique diam. Suspendisse ut placerat augue. 
 Morbi et leo in erat finibus tincidunt. 
 Donec molestie consequat risus, sed faucibus diam imperdiet ac.
Aenean aliquet massa nec velit ornare, pellentesque pretium tellus aliquam. 
Vestibulum eleifend elit sed est aliquet, vitae hendrerit.
"""


def hash_md5(lorem):
    m = hashlib.md5()
    m.update(lorem)
    value = m.hexdigest()
    return value


def hash_sha1(lorem):
    m = hashlib.sha1()
    m.update(lorem)
    value = m.hexdigest()
    return value


def hash_sha256(lorem):
    m = hashlib.sha256()
    m.update(lorem)
    value = m.hexdigest()
    return value


if __name__ == "__main__":
    lorem = bytes(lorem, "UTF-8")

    res = hash_md5(lorem)
    print(f"Hash with MD5: {res}")

    res2 = hash_sha1(lorem)
    print(f"Hash with SHA1: {res2}")

    res3 = hash_sha256(lorem)
    print(f"Hash with SHA256: {res3}")
