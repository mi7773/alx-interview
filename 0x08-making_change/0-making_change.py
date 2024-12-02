#!/usr/bin/python3
'''
0-making_change.py
'''


def makeChange(coins, total):
    remaining = total
    solution = []
    coins.sort(reverse=True)
    while remaining > 0:
        initial = remaining
        for coin in coins:
            if coin <= remaining:
                solution.append(coin)
                remaining -= coin
                break
        if remaining == initial:
            return -1
    return len(solution)
