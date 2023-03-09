def fibonacci(n:int,memo:dict={1:1,2:1,3:2}):
    if n not in memo:
        memo[n] = fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]


