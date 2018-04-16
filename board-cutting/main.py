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
    cost_y = list(map(lambda a: [a, 1], cost_y))
    cost_x = list(map(lambda a: [a, 1], cost_x))

    def done():
        for c in cost_y:
            if c[0] != 0:
                return False
        for c in cost_x:
            if c[0] != 0:
                return False
        return True

    cost = 0
    while not done():
        #print('==============')
        #print('Costs:', cost_y, cost_x)

        largestCost = -1
        for c in cost_y:
            if c[0] > largestCost:
                largestCost = c[0]
        for c in cost_x:
            if c[0] > largestCost:
                largestCost = c[0]

        #print('largest cost', largestCost)

        smallestCutY = -1
        for i, c in enumerate(cost_y):
            if c[0] == largestCost:
                if smallestCutY == -1 or c[1] < cost_y[smallestCutY][1]:
                    smallestCutY = i

        smallestCutX = -1
        for i, c in enumerate(cost_x):
            if c[0] == largestCost:
                if smallestCutX == -1 or c[1] < cost_y[smallestCutX][1]:
                    smallestCutX = i

        #print('smallest y cuts', smallestCutY)
        #print('smallest x cuts', smallestCutX)

        assert smallestCutY == -1 or cost_y[smallestCutY][0] == largestCost
        assert smallestCutX == -1 or cost_x[smallestCutX][0] == largestCost

        if smallestCutX == -1 or (smallestCutY != -1 and cost_y[smallestCutY][1] < cost_x[smallestCutX][1]):
            #print('CUTTING ACROSS Y', smallestCutY, 'cost = ', largestCost)
            cost += cost_y[smallestCutY][1] * largestCost
            #cost_x = list(map(lambda a: (a[0], a[1]+1), cost_x))
            for c in cost_x:
                c[1] += 1

            cost_y[smallestCutY][0] = 0
        else:
            #print('CUTTING ACROSS X', smallestCutX, 'cost = ', largestCost)
            cost += cost_x[smallestCutX][1] * largestCost
            #cost_y = list(map(lambda a: (a[0], a[1]+1), cost_y))
            for c in cost_y:
                c[1] += 1
            cost_x[smallestCutX][0] = 0

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
