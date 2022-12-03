A = 2
B = 7
C = [3,4,2,2,3]
C = [1,2,2,5,3,2]
sum =0
B = 5

A = 12
B = 8
C =[7,1,6,1,1,5,1,1,1,1,1,3,2,1,5,2,1,8,3,3,2,1,2,4,1,3,2,3,4,3,1,7,1,3,4,1]
hm =[0]*(B+1)
for i in range(len(C)):
    sum += C[i]
    hm[sum] += 1
    if sum == B:
        sum =0
print(hm)
max_v = max(hm[:-1])

print(max_v)

