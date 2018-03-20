import sys

def decodings(s, depth=0):
    if len(s) == 0 or len(s) == 1:
        return 1

    if s[0] == '0':
        return 0

    res = decodings(s[1:], depth+1)
    if int(s[:2]) <= 26:
        res += decodings(s[2:], depth+1)

    return res

while True:
    x = input()
    if x == '0':
        break
    print(decodings(x))
