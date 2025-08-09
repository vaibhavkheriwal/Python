"""
You're embarking on a journey through a circular route with n checkpoints. Each checkpoint i is equipped with a certain resource, represented by res[i]. Traveling from checkpoint i to (i + 1) consumes a certain amount of this resource, denoted by cost[i]. You begin your journey with empty supplies at one of the checkpoints. Your task is to find the starting checkpoint index from where you can complete the circuit once in a clockwise direction without exhausting your resources. If such a solution exists, return the index; otherwise, return -1. If there exists a solution, it is guaranteed to be unique.

Example 1:
Input:
res = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output:
3

Example 2:
Input:
res = [2, 3, 4], cost = [3, 4, 3]
Output:
-1
"""

def jurney(res, cost):
    can_start_from = []
    total_res = 0
    total_cost = 0

    for i in range(len(res)):
        total_res += res[i]
        total_cost += cost[i]

    if total_res >= total_cost:

        for i in range(len(res)):
            can_start_from.append(res[i]-cost[i])

            if can_start_from[i] > 0:
                return can_start_from[i]
    
    else:
        return -1

_res = [1, 2, 3, 4, 5]
_cost = [3, 4, 5, 1, 2]
print(jurney(_res, _cost))