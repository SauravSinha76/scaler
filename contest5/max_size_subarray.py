def solve(A):

    n = len(A)

    start = 0
    end =0

    max_size =0
    start_ans =0
    end_ans =0
    for i in range(n):
        if A[i] < 0:
            start = i+1
        else:
            end = i+1
        if end - start + 1 > max_size:
            max_size = end - start + 1
            start_ans = start
            end_ans = end


    return A[start_ans : end_ans]


A = [-1,-5,-6,-1,-7,-6,-8]
# A = [1,2,3,4,5,6]
# A = [8,-5,5,4,2,5,-5,-6,1,2]
print(solve(A))