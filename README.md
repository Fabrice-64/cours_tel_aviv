# Course on Cyber Security by the University of Tel Aviv (Edx)

## Packages needed:
- scapy
- pycryptodome (pycrypto should be removed beforehand)
<br>
Those packages are listed in requirements.txt

## Exercises:
- 01: Use of python eval()
- 02: Crack a password using time elapsed between two characters
- 03: Using brute force to decrypt Caesar Key (one of the lines is a readable text)
- 04: Guess some letters in a text using character frequency (English language)
- 05: Encrypt a string using XOR based cipher and a one time pad (keystream bit used only once)
- 06: fake a RC4 encryption. Model is taken from https://github.com/manojpandey/rc4
- 07: encrypt a message using RC4 with the library pycryptodome. Source in Python2: https://github.com/nemozqqz/pycrypto-sample/blob/master/RC4.py
- 08: encrypt a message using AES and CBC, based on pycryptodome
- 08_v2: a simplified version of the previous exer, dedicated to TAU exercise. Interesting as a breakdown of the previous exercise.
- 09: counts the character frequency in a large string iot to detect whether it's in ENG language.
- 10: crack through brute force an AES_CBC encrypted phone number
