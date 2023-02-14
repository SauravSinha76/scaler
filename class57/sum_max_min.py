from collections import deque


def solve(A,B):
    q = deque()
    ans = 0
    n = len(A)
    for i in range(B):
        if not q:
            q.append(A[i])
        else:
            while q and A[i] > q[-1]:
                q.pop()
            else:
                q.append(A[i])
    ans += q[0]

    for i in range(1, n - B + 1):
        leaving = A[i - 1]
        if q[0] == leaving:
            q.popleft()
        while q and A[i + B - 1] > q[-1]:
            q.pop()
        else:
            q.append(A[i + B - 1])
        ans += q[0]

    q = deque()
    min_ans = 0
    n = len(A)
    for i in range(B):
        if not q:
            q.append(A[i])
        else:
            while q and A[i] < q[-1]:
                q.pop()
            else:
                q.append(A[i])
    ans += q[0]

    for i in range(1, n - B + 1):
        leaving = A[i - 1]
        if q[0] == leaving:
            q.popleft()
        while q and A[i + B - 1] < q[-1]:
            q.pop()
        else:
            q.append(A[i + B - 1])
        ans += q[0]
    return ans

A = [2, 5, -1, 7, -3, -1, -2]
B = 4
# A = [2, -1, 3]
# B = 2
print(solve(A,B))