class Node:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.child = [None] * 26
        self.eow = False

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

def modified_search(root,word):
    curr = root
    for i in range(len(word)):
        idx = ord(word[i]) - ord('a')
        if curr.child[idx] is None:
            return i
        curr = curr.child[idx]
    return curr.eow

def solve(A,B):
    root = Node("-",1)

    for i in range(len(A)):
        insert(root,A[i])

    ans =""
    for i in range(len(B)):
        if modified_search(root,B[i]):
            ans += '1'
        else:
            ans += '0'
    return ans



A = ['data', 'circle', 'cricket']
B = ['date', 'circel', 'crikket', 'data', 'circl']
print(solve(A,B))