def print_inc(A):
    if A == 0:
        return
    print_inc(A-1)
    print(A,end=" ")
def solve(A):
    print_inc(A)
    print()

solve(5)
