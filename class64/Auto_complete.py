
class Node:
    def __init__(self,data,wight):
        self.data = data
        self.eow = False
        self.freq = 1
        self.child = {}
        self.weight = wight

def insert(root,word,weight):
    curr = root
    for w in word:
        if curr.child.get(w,None) is None :
            curr.child[w] = Node(w,weight)
        else:
            curr.child[w].freq += 1
            if curr.child[w].weight < weight:
                curr.child[w].weight = weight
        curr = curr.child[w]
    curr.eow = True

def build(root,ans,word,n):
    new_word = word + root.data
    if root.eow:
        ans.append(new_word)
    for k in root.child.keys():
        build(root.child[k],ans,new_word,n)
def words(root,prefix):
    curr = root
    for w in prefix:
        curr = curr.child[w]
    ans = [prefix]*curr.freq



def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    case = int(input())
    for _ in range(case):
        n,m = map(int, input().split())


        words = input().split()
        root = Node("-")
        for i in range(n):
            insert(root,words[i])

        ans =[]
        print(build(root,ans,"",n))
        print(ans)

    return 0


# if __name__ == '__main__':
#     main()


A = ["abcd", "aecd", "abaa", "abef", "acdcc", "acbcc"]
root = Node("-")
for a in A:
    insert(root,a)

ans= []
print(build(root,ans,"",len(A)))
print(ans)