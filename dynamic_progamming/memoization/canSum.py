from typing import List


def can_sum(target_sum: int, numbers: List, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for n in numbers:
        remainder = target_sum - n
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3]))
