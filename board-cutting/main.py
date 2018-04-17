#!/bin/python3

import sys

def fst(a):
    return a[0]

def snd(a):
    return a[1]

def index(arr, elem):
    try:
        return arr.index(elem)
    except:
        return -1

def boardCutting(cost_y, cost_x):
    cuts_y = 1
    cost_y.sort(reverse=True)
    cuts_x = 1
    cost_x.sort(reverse=True)

    cuts_needed = len(cost_x) + len(cost_y)
    iters = 0
    cost = 0
    while not iters == cuts_needed:
        iters += 1
        #print('==============')
        #print('Costs:', cost_x, cost_y)

        def cuty():
            nonlocal cost
            nonlocal cuts_x
            nonlocal cuts_y
            nonlocal cost_y
            #print('CUTTING ACROSS Y', cuts_y, 'cost = ', cost_y[0])
            cost += cuts_y * cost_y[0]
            cuts_x += 1
            cost_y.pop(0)

        def cutx():
            nonlocal cost
            nonlocal cuts_x
            nonlocal cuts_y
            nonlocal cost_x
            #print('CUTTING ACROSS X', cuts_x, 'cost = ', cost_x[0])
            cost += cuts_x * cost_x[0]
            cuts_y += 1
            cost_x.pop(0)

        #if len(cost_x) == 0 or cost_y[0] > cost_x[0] or (cost_y[0] == cost_x[0] and cuts_y < cuts_x):

        if len(cost_x) == 0:
            cuty()
        elif len(cost_y) == 0:
            cutx()
        elif cost_y[0] > cost_x[0]:
            cuty()
        elif cost_y[0] < cost_x[0]:
            cutx()
        elif cuts_y < cuts_x:
            cuty()
        else:
            cutx()

    return cost % (10**9 + 7)

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        m, n = input().strip().split(' ')
        m, n = [int(m), int(n)]
        cost_y = list(map(int, input().strip().split(' ')))
        cost_x = list(map(int, input().strip().split(' ')))
        result = boardCutting(cost_y, cost_x)
        print(result)
