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
    cuts_y = [1]*len(cost_y)
    cost_y.sort(reverse=True)
    cuts_x = [1]*len(cost_x)
    cost_x.sort(reverse=True)

    cuts_needed = len(cost_x) + len(cost_y)
    iters = 0
    cost = 0
    while not iters == cuts_needed:
        iters += 1
        #print('==============')
        #print('Costs:', cost_y, cost_x)

        if len(cost_x) == 0:
            largestCost = cost_y[0]
        elif len(cost_y) == 0:
            largestCost = cost_x[0]
        else:
            largestCost = max(cost_x[0], cost_y[0])

        #print('largest cost', largestCost)

        smallestCutY = -1
        for i, c in enumerate(cost_y):
            if c != largestCost:
                break
            if smallestCutY == -1 or cuts_y[i] < cuts_y[smallestCutY]:
                smallestCutY = i

        smallestCutX = -1
        for i, c in enumerate(cost_x):
            if c != largestCost:
                break
            if smallestCutX == -1 or cuts_x[i] < cuts_x[smallestCutX]:
                smallestCutX = i

        #if smallestCutY != -1:
        #    print('smallest y cuts', cuts_y[smallestCutY], 'piece')
        #if smallestCutX != -1:
        #    print('smallest x cuts', cuts_x[smallestCutX], 'piece')

        assert smallestCutY == -1 or cost_y[smallestCutY] == largestCost
        assert smallestCutX == -1 or cost_x[smallestCutX] == largestCost

        if smallestCutX == -1 or (smallestCutY != -1 and cuts_y[smallestCutY] < cuts_x[smallestCutX]):
            #print('CUTTING ACROSS Y', smallestCutY, 'cost = ', largestCost)
            cost += cuts_y[smallestCutY] * largestCost
            for i in range(len(cuts_x)):
                cuts_x[i] += 1

            cost_y.pop(0)
            cuts_y.pop(0)
        else:
            #print('CUTTING ACROSS X', smallestCutX, 'cost = ', largestCost)
            cost += cuts_x[smallestCutX] * largestCost
            for i in range(len(cuts_y)):
                cuts_y[i] += 1

            cost_x.pop(0)
            cuts_x.pop(0)

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
