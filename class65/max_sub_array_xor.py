def to_binery(A, length):
    ans =""
    first = False
    for i in range(31,-1,-1):
        if A >> i & 1:
            first = True
            ans += '1'
        elif first:
            ans += '0'
    while len(ans) < length:
        ans = '0' + ans
    return ans

class TriesNode:
    def __init__(self, data):
        self.data = data
        self.child = [None] * 2
        self.index = -1


def insert(root, word, index):

    curr = root

    for i in range(len(word)):
        idx = int(word[i])
        if curr.child[idx] is None:
            curr.child[idx] = TriesNode(word[i])
        curr = curr.child[idx]
    curr.index = index

def solve(A):
    root = TriesNode("-")

    n = len(A)
    ans = A[0]
    index = [0] * 2
    for i in range(1,n):
        A[i] ^= A[i-1]
        if A[i] > ans:
            ans = A[i]
            index[0] = 0
            index[1] = i
    bin = to_binery(ans,0)

    for i in range(n):
        insert(root,to_binery(A[i],len(bin)), i)

    for i in range(n):
        curr = root
        xor =0
        for j in range(len(bin)-1,-1,-1):
            if A[i] >> j & 1:
                if curr.child[0]:
                    xor |= 1 << j
                    curr = curr.child[0]

                else:
                    curr = curr.child[1]
            else:
                if curr.child[1]:
                    xor |= 1 << j
                    curr = curr.child[1]

                else:
                    curr = curr.child[0]

        maxi = max(curr.index, i)
        mini = min(curr.index, i) + 1
        if xor > ans:
            ans = xor
            index[0] = mini
            index[1] = maxi
        elif xor == ans:
            if index[1] - index[0] > maxi - mini:
                index[0] = mini
                index[1] = maxi
            elif index[1] - index[0] == maxi - mini:
                if mini < index[0]:
                    index[0] = mini
                    index[1] = maxi
    index[0] += 1
    index[1] += 1
    return index
    # for i in range(-1,n):
    #     for j in range(i+1,n):
    #         if i == -1 and A[j] == ans:
    #             index[0] = i+2
    #             index[1] = j + 1
    #         if A[i] ^ A[j] == ans:
    #             index[0] = i+ 2
    #             index[1] = j + 1


A = [1, 3, 4]
# A = [8]
A = [ 33, 29, 18 ]
# A = [ 32, 17, 9, 15, 28, 41, 10 ]
print(solve(A))
# print(to_binery(10, 0))


