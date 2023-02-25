def getEndingIndex(str1, n, i):
    i += 1
    while (i < n):

        curr = str1[i]
        prev = str1[i - 1]

        # If the current character appears after
        # the previous character according to
        # the given circular alphabetical order
        if ((curr == 'a' and prev == 'z') or
                (ord(curr) - ord(prev) == 1)):
            i += 1
        else:
            break

    return i - 1

class Pair:
    def __init__(self,len,count):
        self.len = len
        self.count = count

    def __str__(self):
        return f"len= {self.len}, count= {self.count}"

    def __repr__(self):
        return f"len= {self.len}, count= {self.count}"
    def __eq__(self, other):
        if self.len == other.len and self.len == other.len:
            return True
        return False
    def __hash__(self):
        return hash(self.len) + hash(self.count)

def largestSubstr1(str1,B):
    Len = 0
    n = len(str1)
    count = 0
    i = 0
    while (i < n):
        # Valid sub-string exists from
        # index i to end
        end = getEndingIndex(str1, n, i)

        if str1[i] <= B <= str1[end]:
            count += 1
        # Update the Length
        Len = max(end - i + 1, Len)
        i = end + 1
    return Pair(Len,count)


def solve(A,B,C):

    hm ={}

    for i in range(len(A)):
        p= largestSubstr1(A[i],B)
        if p not in hm:
            hm[p] = i

    ans =[]
    for c in C:
        idx = hm.get(Pair(c[0],c[1]),-1)
        if idx == -1:
            ans.append("NULL")
        else:
            ans.append(A[idx])
    return ans

A =["abaclmn","abdwx","aabc","aab","oxyps","ercd"]
B = "a"
C =[
    [3,2],
    [4,2]
]
print(solve(A,B,C))