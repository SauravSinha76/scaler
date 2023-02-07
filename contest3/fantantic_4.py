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
    hm =[0] * 4
    for i in range(n):
        A[i] = A[i] % 4
        hm[A[i] % 4] += 1

    print(hm)
    count =0

    val = min(hm[1],hm[3])
    count += val
    hm[1] -= val
    hm[3] -= val

    while hm[3] >= 2:
        hm[3] -= 2
        hm[2] += 1
        count += 1

    while hm[1] >= 2:
        hm[1] -= 2
        hm[2] += 1
        count += 1


    count += hm[2] // 2
    hm[2] %= 2
    if hm[1] != 0 or hm[2] != 0 or hm[3] != 0:
        return -1
    return count
    # return count


    # A.sort()
    # print(A)
    #
    # low = 0
    # high = n - 1
    # ans =-1
    # while low <= high:
    #     mid = (low + high) // 2
    #
    #     if A[mid] > 0:
    #         high = mid -1
    #     else:
    #         ans = mid
    #         low = mid + 1
    # count = pair_count(A,4)
    # if (n - ans -1)/ 2 == count:
    #     return count
    # else:
    #     return -1



A =[1,3,4,4,2,2]
A =[4,2,2]
A = [1,2,3,1,2,3,8]
# A = [2,2,2,2]
# A = [1,1,3,2]
# A =[2]
# A =[3,3,3,3]
print(solve(A))
