def bestSum(targetSum: int, numbers: list, memo: dict = {}) -> list:
    if targetSum in memo:
        return memo[targetSum][:]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombi = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombi = bestSum(remainder, numbers, memo)

        if remainderCombi is not None:
            remainderCombi.append(num)
            if shortestCombi is None or len(remainderCombi) < len(shortestCombi):
                shortestCombi = remainderCombi[:]

    if shortestCombi:
        memo[targetSum] = shortestCombi[:]
    else:
        memo[targetSum] = None

    return shortestCombi


print(bestSum(100, [1, 2, 5, 25]))
