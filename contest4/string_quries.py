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
    return Len,count


def solve(A,B,C):

    hm ={}

    for i in range(len(A)):
        length,count = largestSubstr1(A[i],B)
        if count in hm:
            if length in hm[count]:
                hm[count][length].append(A[i])
            else:
                hm[count][length] = [A[i]]
        else:
            hm[count] ={length:[A[i]]}
    return hm

A =["abaclmn","abdwx","aabc","aab","oxyps","ercd"]
B = "a"
C =[
    [3,2],
    [4,2]
]
print(solve(A,B,C))