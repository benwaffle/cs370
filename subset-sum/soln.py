import sys

def s(i):
    i.sort()
    m = 1
    for k in i:
        if k > m:
            break
        else:
            m += k
    return m

d = int(sys.stdin.readline())

for x in range(d):
  n = int(sys.stdin.readline())
  ns = list(map(int, sys.stdin.readline().split()))
  assert(len(ns) == n)
  print(s(ns))
