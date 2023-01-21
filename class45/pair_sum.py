def bsearch(A,low,high,ele):
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == ele:
            return mid
        if A[mid] < ele:
            low = mid +1
        else:
            high = mid -1
    return -1

def count_duplicate(A,idx,low,high):
    left = idx
    right = idx + 1
    count =1
    while left > low and A[left] == A[left -1]:
        left -= 1
        count +=1
    while right < high and A[right] == A[right -1]:
        right += 1
        count +=1
    return count


def solve(A,B):
    n = len(A)
    count = 0
    i =0
    j = n-1
    while i < j:
        add = A[i] + A[j]
        if add == B:
            if A[i] != A[j]:
                left_count = 1
                while i < j and A[i] == A[i+1]:
                    left_count += 1
                    i += 1
                right_count =1
                while j > i and A[j] == A[j-1]:
                    right_count += 1
                    j -= 1
                count += left_count * right_count
            else:
                x = j -i + 1
                count += (x*(x-1))// 2
                i,j = j,i
            i += 1
            j -= 1
        elif add < B:
            i += 1
        else:
            j -= 1


    return count

A = [1, 1, 1,1,1,1,1,1]
B = 2
# A = [1, 1]
# B = 2
# A = [ 2, 3, 3, 5, 7, 7, 8, 9,9 ,10, 10 ]
# B = 11
# A = [ 2, 3, 5, 6, 10 ]
# B = 6
# A = [ 2, 2, 3, 4, 4, 5, 6, 7, 10 ]
# B = 8
print(solve(A,B))