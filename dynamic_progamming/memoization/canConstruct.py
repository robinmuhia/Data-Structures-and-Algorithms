def can_construct(target:str,word_bank:list,memo:dict={})->bool:
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]                
                if can_construct(suffix,word_bank,memo):
                    memo[target] = True
                    return True
        except:
            continue

    memo[target] = False
    return False


