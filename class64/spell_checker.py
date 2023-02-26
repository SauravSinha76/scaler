class Node:
    def __init__(self,data):
        self.data = data
        self.eow = False
        self.child = [None] * 26


def insert(root,word):
    curr = root
    for w in word:
        idx = ord(w) - ord('a')
        if curr.child[idx] is None:
            curr.child[idx] = Node(w)
        curr = curr.child[idx]
    curr.eow = True

def search(root,word):
    curr = root
    for w in word:
        idx = ord(w) - ord('a')
        if curr.child[idx] is None:
            return False
        curr = curr.child[idx]
    return curr.eow
def solve(A,B):
    root = Node('-')
    for i in range(len(A)):
        insert(root,A[i])

    ans = []
    for i in range(len(B)):
        if search(root,B[i]):
            ans.append(1)
        else:
            ans.append(0)
    return ans

A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
A = [ "tape", "bcci" ]
B = [ "table", "cci" ]
print(solve(A,B))

