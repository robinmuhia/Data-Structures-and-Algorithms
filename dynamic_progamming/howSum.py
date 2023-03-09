def how_sum(target_sum:int,numbers:list,memo:dict={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    
    for n in numbers:
        rem = target_sum - n
        result = how_sum(rem,numbers,memo)
        if result != None:
            result.append(n)
            memo[target_sum] = result
            return result
        
    memo[target_sum] = None
    return None


