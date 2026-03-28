naive_calls = 0
memo_calls = 0
memo = {}

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return n
    return fib_naive(n-1) + fib_naive(n-2)

def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

for val in [10, 20]:
    naive_calls = 0
    memo_calls = 0
    print(f"n={val} | Naive result: {fib_naive(val)} (Calls: {naive_calls}) | Memo result: {fib_memo(val)} (Calls: {memo_calls})")