def reverse(A,index):
    if index == -1:
        return
    print(A[index],end="")
    reverse(A,index-1)

my_string = input()
reverse(my_string,len(my_string)-1)
