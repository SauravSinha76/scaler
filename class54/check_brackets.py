def solve(A,B):

    hm1= {}
    hm2 ={}
    stack =[]
    global_sign = True
    for a in A:
        if a == '(' and len(stack) != 0 and stack[-1] == '-':
            global_sign = not global_sign
            stack.pop()
        elif a == ')':
            global_sign = not  global_sign
        elif a.isalpha():
            if len(stack) != 0 and stack[-1] == '-':
                if global_sign:
                    hm1[a] = False
                else:
                    hm1[a] = True
                stack.pop()
            else:
                hm1[a] = global_sign
        else:
            stack.append(a)
    stack = []
    global_sign = True
    for a in B:
        if a == '(' and len(stack) != 0 and stack[-1] == '-':
            global_sign = not global_sign
            stack.pop()
        elif a.isalpha():
            if len(stack) != 0 and stack[-1] == '-':
                if global_sign:
                    hm2[a] = False
                else:
                    hm2[a] = True
                    stack.pop()
            else:
                hm2[a] = global_sign
        else:
            stack.append(a)
    if hm1 == hm2:
        return 1
    else:
        return 0
A = "-(a+b+c)"
B = "-a-b-c"
A = "a-b-(c-d)"
B = "a-b-c-d"
A = "-(-(-(-a+b)-d+c)-q)"
B = "a-b-d+c+q"
A = "-(a+((b-c)-(d+e)))"
B = "-(a+b-c-d-e)"
print(solve(A,B))





