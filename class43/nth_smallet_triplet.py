def count_less_then(A,ele):
    count =0
    for i in range(len(A)):
        if A[i] < ele:
            count += 1
    return count

def get_element(triplet,B):
    min_val = min(triplet)
    max_val = max(triplet)
    ans =0
    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        pos = count_less_then(triplet, mid)

        if pos <= B:
            ans = mid
            min_val = mid + 1
        else:
            max_val = mid -1
    return ans

def solve(A):
    n = len(A)
    triplet = []

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                triplet.append(A[i]+A[j]+A[k])


    return get_element(triplet,B-1)

A = [2, 4, 3, 2]
B = 3
A = [1, 5, 7, 3, 2]
B = 9
print(solve(A))
