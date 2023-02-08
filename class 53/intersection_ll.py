def solve(A,B):

    len_A = 0
    len_B = 0

    h1 = A
    h2 = B

    while h1:
        h1 = h1.next
        len_A += 1

    while h2:
        h2 = h2.next
        len_B += 1

    h1 = A
    h2 = B
    if len_A > len_B:
        diff = len_A - len_B

        while h1 and diff > 0:
            h1 = h1.next
            diff -= 1
    else:
        diff = len_B - len_A

        while h2 and diff > 0:
            h2 = h2.next
            diff -= 1


    while h1 and h2:
        if h1 == h2:
            return h1
        h1 = h1.next
        h2 = h2.next

    return None


