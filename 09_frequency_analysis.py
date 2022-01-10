from collections import Counter

ENG_1 = """
Do in laughter securing smallest sensible no mr hastened. 
As perhaps proceed in in brandon of limited unknown greatly. 
Distrusts fulfilled happiness unwilling as explained of difficult. 
No landlord of peculiar ladyship attended if contempt ecstatic. 
Loud wish made on is am as hard. Court so avoid in plate hence. 
Of received mr breeding concerns peculiar securing landlord. 
Spot to many it four bred soon well to. Or am promotion in no departure abilities. 
Whatever landlord yourself at by pleasure of children be.
"""

ENG_2 = """
Increasing impression interested expression he my at. 
Respect invited request charmed me warrant to. 
Expect no pretty as do though so genius afraid cousin. 
Girl when of ye snug poor draw. Mistake totally of in chiefly. 
Justice visitor him entered for. 
Continue delicate as unlocked entirely mr relation diverted in. 
Known not end fully being style house. 
An whom down kept lain name so at easy.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
most_freq_eng = "etaion"


def is_ascii(s):
    return s.isascii()


def is_english(dict_chars):
    counter = 0
    desc_freq_chars = list(sorted(dict_chars.items(), key=lambda x: x[1], reverse=True))
    for item in desc_freq_chars:
        if item[0] not in alphabet:
            desc_freq_chars.remove(item)
    for item in desc_freq_chars[:3]:
        if item[0] in most_freq_eng:
            counter += 1
    if counter == 3:
        return True
    else:
        return False


if __name__ == "__main__":
    if is_ascii(ENG_2):
        ENG_2 = ENG_2.lower()
        count_char = Counter(ENG_2)
        value = is_english(count_char)
        print(value)
    else:
        print("Your string includes non ASCII Characters. Please correct it before proceeding.")
