def canConstruct(x, y):
    arr = [False for _ in range(len(x) + 1)]
    arr[0] = True

    for i in range(len(x) + 1):
        if arr[i] == True:
            for j in y:
                if x[i : i + len(j)] == j:
                    arr[i + len(j)] = True

    return arr[len(x)]


print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
