n = 127
count =0
while n >0:
    for j in range(n):
        n //= 2
        count +=1

print(count)