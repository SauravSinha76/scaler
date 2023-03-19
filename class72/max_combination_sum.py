def solve1(i, n, A, total):
    if i == n:
        print(total)
        return
    total += A[i]
    solve1(i + 1, n, A, total)
    total -= A[i]
    solve1(i + 1, n, A, total)

def solve2(i, A):
    if i < 0:
        return 0
    if i == 0:
        return A[i]

    pick = A[i] + solve2(i - 2, A)

    not_pick = solve2(i - 1, A)

    return max(pick, not_pick)

def mem_solve(i, A, dp):
    if i < 0:
        return 0
    if i == 0:
        return A[0]

    if dp[i] != -1:
        return dp[i]
    pick = A[i] + mem_solve(i - 2, A, dp)
    not_pick = A[i - 1]
    dp[i] = max(pick, not_pick)
    return dp[i]

def tab_solve(A, dp):
    n = len(A)
    dp[0] = A[0]

    for i in range(1, n):
        pick = A[i]
        if i > 1:
            pick += dp[i - 2]
        not_pick = dp[i - 1]
        dp[i] = max(pick, not_pick)

    return dp[n - 1]

def sp_op_solve(A):
    n = len(A)
    dp_1 =A[0]
    dp_2 =0

    for i in range(1,n):
        pick = A[i]
        if i>1:
            pick += dp_2
        not_pick = dp_1
        dp_2 = dp_1
        dp_1 = max(pick,not_pick)
    return dp_1


def solve(A):
    max_arr =[]

    for i in range(len(A[0])):
        max_arr.append(max(A[0][i], A[1][i]))

    # return  solve2(len(max_arr)-1, max_arr)
    dp = [-1] * (len(max_arr))
    # return mem_solve(len(max_arr)-1, max_arr,dp)
    return sp_op_solve(max_arr)
    # def adjacent(self, A):
    #
    #     dp = [-1] * len(A[0])
    #     max_adjcent_arr = []
    #     for ele in range(len(A[0])):
    #         max_adjcent_arr.append(max(A[1][ele], A[0][ele]))
    #
    #     def maxSumValue(arr_len):
    #         if arr_len < 1:
    #             return max_adjcent_arr[0]
    #         if arr_len == 1:
    #             return max(max_adjcent_arr[0], max_adjcent_arr[1])
    #
    #         if dp[arr_len] == -1:
    #             dp[arr_len] = max(maxSumValue(arr_len - 1), max_adjcent_arr[arr_len] + maxSumValue(arr_len - 2))
    #
    #         return dp[arr_len]
    #
    #     return maxSumValue(len(max_adjcent_arr) - 1)

A =[[1, 2, 3, 4],
    [2, 3, 4, 5]
    ]
print(solve1(0,len(A),A,0))
print(solve(A))