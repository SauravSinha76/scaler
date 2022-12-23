def is_over_lapping(A,B,C,D,E,F,G,H):
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


def area(A,B,C,D,E,F,G,H):
    if is_over_lapping(A,B,C,D,E,F,G,H):
        x1 = max(A,E)
        x2 = min(C,G)

        y1 = max(B,F)
        y2 = min(D,H)

        return (x1 - x2) * (y1 - y2)
    else:
        return 0

A = 0
B = 0
C = 4
D = 4
E = 2
F = 2
G = 6
H = 6

A = 0
B = 0
C = 4
D = 4
E = 2
F = 2
G = 3
H = 3
print(area(A,B,C,D,E,F,G,H))