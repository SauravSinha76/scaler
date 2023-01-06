def solve(A):
    A.sort()
    hm = {}
    used = set()
    for i in range(len(A)):
        hm[A[i]] = hm.get(A[i],0) + 1
        used.add(A[i])
    count =0
    max_used =0
    for key in hm:
        if hm.get(key) > 1:
            duplicate = hm[key] - 1
            i = max(key + 1,max_used)
            while duplicate > 0:
                if i not in used:
                    count += i - key
                    used.add(i)
                    duplicate -= 1
                    max_used = i
                i += 1

    return count

A =[1,1,1,7]
A = [2, 4, 5]
A = [ 51, 6, 10, 8, 22, 61, 56, 48, 88, 85, 21, 98, 81, 76, 71, 68, 18, 6, 14, 23, 72, 18, 56, 30, 97, 100, 81, 5, 99, 2, 85, 67, 46, 32, 66, 51, 76, 53, 36, 31, 81, 56, 26, 75, 69, 54, 54, 54, 83, 41, 86, 48, 7, 32, 85, 23, 47, 23, 18, 45, 79, 95, 73, 15, 55, 16, 66, 73, 13, 85, 14, 80, 39, 92, 66, 20, 22, 25, 34, 14, 51, 14, 17, 10, 100, 35, 9, 83, 31, 60, 24, 37, 69, 62 ]
# A =[ 3, 2, 1, 2, 1, 2, 6, 7]
print(solve(A))