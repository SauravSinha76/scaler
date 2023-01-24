def solve(A):
    n = len(A)
    res = []
    for i in range(n):
        for j in range(i, n):
            sub = []
            for k in range(i, j + 1):
                if A[k] not in sub:
                    sub.append(A[k])
            res.append(sub)
    return res


def countDistictSubarray(arr, n):

    # Count distinct elements in whole array
    vis = dict()
    for i in range(n):
        vis[arr[i]] = 1
    k = len(vis)

    # Reset the container by removing
    # all elements
    vid = dict()

    # Use sliding window concept to find
    # count of subarrays having k distinct
    # elements.
    ans = 0
    right = 0
    window = 0
    for left in range(n):

        while (right < n and window < k):

            if arr[right] in vid.keys():
                vid[arr[right]] += 1
            else:
                vid[arr[right]] = 1

            if (vid[arr[right]] == 1):
                window += 1

            right += 1

        # If window size equals to array distinct
        # element size, then update answer
        if (window == k):
            ans += (n - right + 1)

        # Decrease the frequency of previous
        # element for next sliding window
        vid[arr[left]] -= 1

        # If frequency is zero then decrease
        # the window size
        if (vid[arr[left]] == 0):
            window -= 1

    return ans

def count_dictint(A):
    n = len(A)
    unique = set()
    i =0
    j =0
    count = 0
    while j < n:
        if A[j] in unique:
            unique.remove(A[j])
            i += 1
        else:
            unique.add(A[j])
            count += (j - i + 1)
            j += 1
    return count

A = [1, 1, 3]
# A = [2, 1, 2]
print(solve(A))
print(countDistictSubarray(A,len(A)))
print(count_dictint(A))