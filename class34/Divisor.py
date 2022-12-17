def gcd(A,B):
    if B == 0:
        return A
    return gcd(B, A%B)

def solve(A,B,C):
    lcm = B*C // gcd(B,C)

    count =0
    i =2
    val =lcm
    while val <= A:
        val = lcm * i
        i += 1
        count +=1
    return count
A = 81991
B = 2549
C = 7

# A = 12
# B = 2
# C = 3
print(gcd(B,C))
print(solve(A,B,C))
