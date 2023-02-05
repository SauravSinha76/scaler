def count_student(A,page):
    count = 1
    page_left = page

    for i in range(len(A)):
        if A[i] > page:
            return -1
        if A[i] <= page_left:
            page_left -= A[i]
        else:
            count += 1
            page_left = page - A[i]
    return count



def solve(A,B):
    n = len(A)
    if B > n:
        return -1
    r = sum(A)
    l = max(A)
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        s = count_student(A, mid)

        if s <= B:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans



A = [12, 34, 67, 90]
B = 2

# A = [ 31, 14, 19, 75 ]
# B = 12
# A = [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26
print(solve(A,B))