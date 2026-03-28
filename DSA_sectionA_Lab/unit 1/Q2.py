def complexity_drill(n):
    # 1. Single Loop: O(n)
    count1 = 0
    for i in range(n):
        count1 += 1
    print(f"Single Loop: {count1} ops -> O(n) (Linear)")
    
    # 2. Nested Loop: O(n^2)
    count2 = 0
    for i in range(n):
        for j in range(n):
            count2 += 1
    print(f"Nested Loop: {count2} ops -> O(n^2) (Quadratic)")
    
    # 3. Triangular Loop: O(n^2)
    count3 = 0
    for i in range(n):
        for j in range(i):
            count3 += 1
    print(f"Triangular Loop: {count3} ops -> O(n^2) (Quadratic, ~n^2/2 ops)")
    
    # 4. Halving Loop: O(log n)
    count4 = 0
    i = n
    while i > 0:
        count4 += 1
        i //= 2
    print(f"Halving Loop: {count4} ops -> O(log n) (Logarithmic)")

complexity_drill(10)