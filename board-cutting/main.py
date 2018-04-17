#!/bin/python3

import sys

def boardCutting(cost_y, cost_x):
    cuts_y = cuts_x = 1
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)

    cost = 0
    while cost_x and cost_y:
        if cost_y[0] >= cost_x[0]:
            cost += cuts_y * cost_y[0]
            cuts_x += 1
            cost_y.pop(0)
        else:
            cost += cuts_x * cost_x[0]
            cuts_y += 1
            cost_x.pop(0)

    if cost_x:
        cost += sum(cost_x * cuts_x)
    if cost_y:
        cost += sum(cost_y * cuts_y)

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
