def ceiling(A,low,high,idx):
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == idx:
            return mid
        elif A[mid] < idx:
            low = mid + 1
        else:
            high = mid -1
    return low

def floor(A,low,high,idx):
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == idx:
            return mid
        elif A[mid] < idx:
            low = mid + 1
        else:
            high = mid -1
    return high

def solve(A,B):
    n = len(A)
    index = []
    ans =[]
    for i in range(len(A)):
        if A[i] == '1':
            index.append(i+1)
    for b in B:
        op = b[0]
        idx = b[1]

        if op == 1:
            if idx in index:
                index.remove(idx)
            else:
                index.append(idx)
        else:
            index.sort()
            left = ceiling(index,0,len(index)-1,idx)
            right = left -1
            if left >= len(index) and right < 0:
                ans.append(-1)
            elif left < len(index) and right < 0:
                ans.append(index[left])
            elif left >= len(index) and right > -1:
                ans.append(index[right])
            else:
                if index[left] - idx < idx - index[right]:
                    ans.append(index[left])
                else:
                    ans.append(index[right])

    return ans


A = "10010"
B = [[1, 2],
     [2, 3]]
# A = "010000100"
# B = [[2, 5],
#      [1, 7],
#      [2, 9]]
A = "10010"
B = [
  [1, 3],
  [1, 3],
  [2, 4],
  [2, 2],
  [1, 1],
  [2, 3],
  [1, 5],
  [1, 5]
]
A = "01011"
B = [
  [2, 3],
  [2, 1],
  [1, 4],
  [2, 4],
  [2, 5],
  [1, 2],
  [1, 4],
  [2, 1],
  [2, 3]
]
#
A = "10001010"
B = [
  [2, 5],
  [1, 5],
  [2, 5],
  [1, 7],
  [2, 8],
  [1, 2],
  [2, 5],
  [1, 2],
  [1, 1],
  [2, 4],
  [1, 4],
  [1, 3]
]
#
# A = "111100100011001011000001111111000011101100101111101001101001001010110110011011"
# B = [
#   [2, 9],
#   [1, 11],
#   [1, 15],
#   [2, 56],
#   [1, 26],
#   [1, 14],
#   [2, 24],
#   [1, 45],
#   [2, 30],
#   [2, 16],
#   [2, 66],
#   [2, 67],
#   [1, 21],
#   [2, 20],
#   [2, 56],
#   [2, 2],
#   [1, 78],
#   [1, 3],
#   [1, 70],
#   [1, 16],
#   [1, 47],
#   [2, 23],
#   [1, 61],
#   [1, 9],
#   [2, 30],
#   [2, 37],
#   [1, 46],
#   [1, 4],
#   [1, 49],
#   [2, 2],
#   [2, 32],
#   [2, 25],
#   [1, 35],
#   [1, 41],
#   [2, 39],
#   [1, 48],
#   [1, 59],
#   [2, 77],
#   [1, 68],
#   [1, 77],
#   [1, 36],
#   [1, 6],
#   [1, 58],
#   [1, 15],
#   [1, 64],
#   [1, 63],
#   [1, 63],
#   [2, 60],
#   [2, 66],
#   [1, 25],
#   [1, 38],
#   [2, 64],
#   [1, 44],
#   [1, 52],
#   [2, 8],
#   [2, 78],
#   [1, 17],
#   [1, 47],
#   [2, 6],
#   [2, 69],
#   [2, 17],
#   [2, 63],
#   [2, 32],
#   [1, 17],
#   [2, 14],
#   [2, 23],
#   [2, 9],
#   [2, 7],
#   [2, 53],
#   [1, 18],
#   [1, 36],
#   [1, 29],
#   [2, 77],
#   [2, 9],
#   [2, 61],
#   [2, 75],
#   [2, 66],
#   [2, 40],
#   [1, 55],
#   [2, 36],
#   [1, 45],
#   [1, 10],
#   [1, 11],
#   [2, 46],
#   [1, 57],
#   [1, 58],
#   [1, 44],
#   [2, 59],
#   [2, 54],
#   [1, 48],
#   [1, 23],
#   [2, 69],
#   [1, 44],
#   [2, 40]
# ]

print(solve(A,B))