def solve():
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])
    q = int(line1[2])

    column =[]
    for j in range(m):
        column.append(j)
    row =[]
    for i in range(n):
        row.append(i)

    for i in range(q):
        line = input().split()
        idx = int(line[0])
        if idx == 1:
            c1 = int(line[1])-1
            c2 = int(line[2])-1

            column[c1],column[c2] = column[c2],column[c1]
        elif idx == 2:
            r1 = int(line[1])-1
            r2 = int(line[2])-1

            row[r1],row[r2] = row[r2],row[r1]

        elif idx == 3:
            x1 = int(line[1])-1
            y1 = int(line[2])-1
            x2 = int(line[3])-1
            y2 = int(line[4])-1

            print(row[x1] *m + column[y1]+1)
            print(row[x2] *m +column[y2]+1)
        else:
            x1 = int(line[1])-1
            y1 = int(line[2])-1
            x2 = int(line[3])-1
            y2 = int(line[4])-1

            print(row[x1] * m + column[y1]+1)
            print(row[x2] * m + column[y2]+1)

solve()