class Node:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.child = [None] * 26

def insert(root,word):
    curr = root
    for w in word:
        idx = ord(w) - ord('a')
        if curr.child[idx] is None:
            curr.child[idx] = Node(w,1)
        else:
            curr.child[idx].freq += 1
        curr = curr.child[idx]
    curr.eow = True

def get_prefix(root,word):
    curr = root
    for i in range(len(word)):
        idx = ord(word[i]) - ord('a')
        if curr.child[idx] is None:
            return 0
        curr = curr.child[idx]
    return curr.freq
def solve(A,B):

    root = Node("-",1)
    ans=[]
    for i in range(len(A)):
        if A[i] ==0:
            insert(root,B[i])
        else:
            ans.append(get_prefix(root,B[i]))

    return ans

A = [0, 0, 1, 1]
B = ["hack", "hacker", "hac", "hak"]
A = [0, 1]
B = ["abcde", "abc"]
print(solve(A,B))