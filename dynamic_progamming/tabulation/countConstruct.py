def count_construct(x,y):
    arr = [0 for _ in range(len(x)+1)]
    arr[0] = 1
    
    for i in range(len(x)+1):
        if arr[i] != 0:
            for j in y:
                if x[i:i+len(j)] == j:                    
                    arr[i+len(j)] += arr[i]
                        
    return arr[len(x)]


print(count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(count_construct('purple',['purp','p','ur','le','purpl']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee']))