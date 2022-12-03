import functools

class Student:
    def __init__(self,x):
        self.name = x
        self.marks = get_number(x)

def get_number(x):
    i = 1
    while i < 4:
        if '0' > x[-i] or x[-i] > '9':
            break
        i += 1
    return int(x[-i+1:])
def comprator(x,y):

    if x.marks < y.marks:
        return -1
    else:
        return 1

def solve(A):
    students = []
    for a in A:
        students.append(Student(a))
    students.sort(key=functools.cmp_to_key(comprator),reverse=True)
    A = []
    for student in students:
        A.append(student.name)
    return A
A =["adarsh80","harsh95","shivam95"]
print(solve(A))