def pair_count(A,B):
    n = len(A)
    count = 0
    i = 0
    j = n - 1
    while i < j:
        add = A[i] + A[j]
        if add == B:
            if A[i] != A[j]:
                count += 1
                while i < j and A[i] == A[i + 1] and A[j] == A[j - 1]:
                    count += 1
                    i += 1
                    j -= 1
            else:
                x = j - i + 1
                count += x// 2
                i, j = j, i
            i += 1
            j -= 1
        elif add < B:
            i += 1
        else:
            j -= 1

    return count
def solve(A):

    n = len(A)

    for i in range(n):
        A[i] = A[i] % 4

    A.sort()
    print(A)

    low = 0
    high = n - 1
    ans =-1
    while low <= high:
        mid = (low + high) // 2

        if A[mid] > 0:
            high = mid -1
        else:
            ans = mid
            low = mid + 1
    count = pair_count(A,4)
    if (n - ans -1)/ 2 == count:
        return count
    else:
        return -1



A =[1,3,4,4,2,2]
A =[4,2,2]
A = [1,2,3,1,2,3,8]
A = [2,2,2,2]
A = [1,1,3,2]
A =[2]
A =[3,3,3,3]
print(solve(A))
