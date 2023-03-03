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
    max_of_A = max(A)
    bin = to_binery(max_of_A,0)

    for i in range(n):
        insert(root,to_binery(A[i],len(bin)), i)

    ans = 0
    index =[-1] * 2
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
        if xor > ans:
            ans = xor
            index[0] = i
            index[1] = curr.index
    print(index)
    return ans

A = [1, 2, 3, 4, 5]
# A = [5, 17, 100, 11]
print(solve(A))
# print(to_binery(10, 0))


