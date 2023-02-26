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
        if curr.data != '-' and curr.freq == 1:
            return word[:i]
        curr = curr.child[idx]
    if curr.freq == 1:
        return word
    return None
def solve(A):

    root =Node("-",1)
    ans = []
    for a in A:
        insert(root,a)

    for a in A:
        ans.append(get_prefix(root,a))

    return ans
A = ["zebra", "dog", "duck", "dove"]
A = ["apple", "ball", "cat"]
print(solve(A))

