def solve(A):
    n = len(A)
    ans =0
    start =0
    end =0
    max_i = -1
    max_j =-1
    for i in range(n):
        if A[i] < 0:
            start = i+1
        else:
            end = i+1
            if ans < (end - start):
                ans = (end - start)
                max_i = start
                max_j = end


    return A[max_i:max_j]

def solve1(A):
    n = len(A)
    count =0
    for i in range(n):
        if A[i] >= 0:
            count += 1

    if count == n:
        return A
    if count == 0:
        return []

    sub_len =0
    start =-1
    end =-1
    for i in range(n):
        if A[i] < 0:
            left =0
            for j in range(i-1,-1,-1):
                if A[j] >= 0:
                    left +=1
                else:
                    break
            if sub_len < left:
                sub_len = left
                start = i -left
                end = i +1

            right = 0
            for j in range(i+1,n):
                if A[j] >= 0:
                    right += 1
                else:
                    break

            if sub_len < right:
                sub_len = right
                start = i +1
                end = i + right +1

    return A[start:end]

A = [5, 6, -1, 7, 8]
# print(A[0:3])
# A = [1, 2, 3, 4, 5, 6]
# A = [ -5173778, -8176176, 1694510, 7089884, -1394259, 1146372, -2502339, 1544618, 6602022, 4330572 ]
print(solve1(A))