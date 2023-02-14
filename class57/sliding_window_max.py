from collections import deque


def solve(A,B):

    n = len(A)

    ans =[]
    start = 0
    end = B
    while end <= n:
        ans.append(max(A[start:end]))
        start += 1
        end += 1

    return ans

def solve1(A,B):
    q = deque()
    ans = []
    n = len(A)
    for i in range(B):
        if not q:
            q.append(A[i])
        else:
            while q and A[i] < q[-1]:
                q.pop()
            else:
                q.append(A[i])
    ans.append(q[0])

    for i in range(1, n - B + 1):
        leaving = A[i - 1]
        if q[0] == leaving:
            q.popleft()
        while q and A[i + B - 1] < q[-1]:
            q.pop()
        else:
            q.append(A[i + B - 1])
        ans.append(q[0])
    return ans
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
B = 6
print(solve(A,B))
print(solve1(A,B))
