class Rectangle:
    length = 0
    breadth = 0

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def isSquare(self):
        return self.length == self.breadth


A = [2,5,1,6,2]
B = [4,5,3,6,2]

rec =[]

for i in range(len(A)):
    rec.append(Rectangle(A[i],B[i]))
ans =[]
for i in range(len(A)):
    count =0
    for j in range(0,i):
        if rec[j].isSquare() and rec[j].area() > rec[i].area():
            count +=1
    ans.append(count)
print(ans)

ans = []
squre_count = {}
for i in range(len(rec)):
    ans.append(squre_count)

    if rec[i].isSquare():
        area = rec[i].area()
        if area in squre_count:
            squre_count[area] += 1
        else:
            squre_count[area] = 1

print(ans)

