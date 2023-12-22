def all_construct(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word) :]
            suffixWays = all_construct(suffix, words)
            targetWays = list(map(lambda way: [word, *way], suffixWays))
            result.extend(targetWays)

    memo[target] = result
    return result
