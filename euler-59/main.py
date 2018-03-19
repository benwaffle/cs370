from itertools import cycle

nums = list(map(chr, map(int, open('cipher.txt').read().split(','))))

cs = 'abcdefghijklmnopqrstuvwxyz'

def crypt(txt, key):
    out = ''
    for i in range(len(txt)):
        out += chr(ord(txt[i]) ^ ord(key[i % len(key)]))
    return out

for a in cs:
    for b in cs:
        for c in cs:
            key = a+b+c
            txt = crypt(nums, key)
            if 'Gospel' in txt:
                print(key, txt)
