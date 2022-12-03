def solve(A):
    n = len(A)
    count =0
    for i in range(n):
        if A[i] == '1':
            count += 1
    if count == n:
        return n
    if count == 0:
        return 0
    ans =0
    for i in range(n):
        if A[i] == '0':
            left =0
            for j in range(i-1,-1,-1):
                if A[j] == '1':
                    left += 1
                else:
                    break
            right = 0
            for j in range(i+1,n):
                if A[j] == '1':
                    right += 1
                else:
                    break

            k = left + right
            if k == count:
                return k
            elif ans < k+1:
                ans = k+1

    return ans

A = "11010110000000000"
print(solve(A))