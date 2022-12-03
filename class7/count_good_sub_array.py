def solve(A,B):
    n = len(A)
    count =0
    for i in range(n):
        sum =0
        sub_len =0
        for j in range(i,n):
            sum += A[j]
            sub_len += 1
            if sub_len %2 ==0 and sum < B:
                count += 1
            elif sub_len % 2 != 0 and sum > B:
                count += 1
    return count

# A = [1, 2, 3, 4, 5]
# B = 4

A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(solve(A,B))