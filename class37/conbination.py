def sub(arr,n,B,x,ans):
    if n == B:
        print(x)
        return

    x.append(arr[n])
    sub(arr,n+1,B,x,ans)
    x.pop()
    sub(arr, n + 1, B,x, ans)

def solve(A,B):
    arr =[]
    for i in range(A):
        arr.append(i+1)
    ans =[]
    x =[]
    sub(arr,0,B,x,ans)
    print(ans)


def subsequence(text, subseq_length):
  if subseq_length <= 0:
    return []

  if subseq_length == 1:
    return list(text)

  text_length = len(text)
  res = []
  tail_length = subseq_length - 1
  for i in range(0, text_length - tail_length):
    for tail in subsequence(text[i+1:], tail_length):
      res.append(text[i] + tail)
  return res


def subsequence_arr(arr, subseq_length):
  if subseq_length <= 0:
    return []

  if subseq_length == 1:
    return list(arr)

  text_length = len(arr)
  res = []
  tail_length = subseq_length - 1
  for i in range(0, text_length - tail_length):
    for tail in subsequence(arr[i+1:], tail_length):
        res.append([arr[i],tail])
  return res

print(subsequence('hey', 2))
print(subsequence('hello', 3))

def solve1(A,B):
    arr =[]
    for i in range(A):
        arr.append(i+1)
    print(subsequence_arr(arr,B))

solve1(4,2)

ans = []
tmp = []

def makeCombiUtil(n, left, k):
    # Pushing this vector to a vector of vector
    if (k == 0):
        ans.append(list(tmp))
        for i in range(len(tmp)):
            print(tmp[i], end=" ")
        print()
        return

    # i iterates from left to n. First time
    # left will be 1
    for i in range(left, n + 1):
        tmp.append(i)
        makeCombiUtil(n, i + 1, k - 1)

        # Popping out last inserted element
        # from the vector
        tmp.pop()


def makeCombi(n, k):
    makeCombiUtil(n, 1, k)
    return ans


# given number
n = 4
k = 2
ans = makeCombi(n, k)
print(ans)