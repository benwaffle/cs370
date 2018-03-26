precedence = '+-*/'
def rpn(st):
    q = []
    s = []

    def peek(d):
        return d[-1]

    def qpush(x):
        nonlocal q
        q = [x] + q
    def qpop():
        return q.pop()

    def spush(x):
        s.append(x)
    def spop():
        return s.pop()

    for c in st:
        if c in '+-*/':
            o1 = c
            while peek(s) in '+-*/' and precedence[o1] <= precedence[peek(s)]:
                qpush(spop())
            spush(o1)
        elif c == '(':
            spush(c)
        elif c == ')':
            while peek(s) != '(':
                qpush(spop())
            spop()
        else:
            qpush(c)

    while len(s) != 0:
        qpush(spop())

    print(''.join(q[::-1]))

for _ in range(int(input())):
    rpn(input())
