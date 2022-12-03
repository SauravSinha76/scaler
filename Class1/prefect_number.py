def solve(A):
    sum =0
    i =1
    while i*i <= A:
        if A % i == 0:
          sum += i
          if A//i != i and i != 1:
              sum += A//i
        i += 1
    if sum == A:
        return 1
    else:
        return 0

for i in range(1,1000):
    if solve(i):
        print(i)