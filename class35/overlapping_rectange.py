def solve(A,B,C,D,E,F,H,G):

    # if rectangle has area 0, no overlap
    if A == C or B == D or E == G or F == H:
        return 0

    # If one rectangle is on left side of other
    if A >= G or E >= C:
        return 0

    # If one rectangle is above other
    if B >= H or F >= D:
        return 0

    return 1


# A = 0
# B = 0
# C = 4
# D = 4
# E = 2
# F = 2
# G = 6
# H = 6

# A = 0
# B = 0
# C = 4
# D = 4
# E = 2
# F = 2
# G = 3
# H = 3

# A = 12
# B = 47
# C = 39
# D = 72
# E = 8
# F = 3
# G = 47
# H = 55

# A = 0
# B = 0
# C = 1
# D = 1
# E = 1
# F = 1
# G = 6
# H = 6

A = 606
B = 133
C = 981
D = 616
E = 614
F = 183
G = 949
H = 614
print(solve(A,B,C,D,E,F,G,H))