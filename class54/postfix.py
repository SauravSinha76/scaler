class Conversion:

    def __init__(self):
        self.stack = []
        self.output = []
        self.precedance = {"+": 1,
                           "-": 1,
                           "*": 2,
                           "/": 2,
                           "^": 3}

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

    def peek(self):
        return self.stack[-1]

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop()

    def isOprand(self, a):
        return a.isalpha()

    def greater(self, a):
        return self.precedance.get(a, 0) <= self.precedance.get(self.peek(), 0)

    def postfix(self, A):

        for a in A:
            if self.isOprand(a):
                self.output.append(a)

            elif a == '(':
                self.push(a)

            elif a == ')':
                while not self.isEmpty() and self.peek() != '(':
                    self.output.append(self.pop())

                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            else:
                while not self.isEmpty() and self.greater(a):
                    self.output.append(self.pop())
                self.push(a)

        while not self.isEmpty():
            self.output.append(self.pop())

        return "".join(self.output)


c = Conversion()
A = "x^y/(a*z)+b"
A = "a+b*(c^d-e)^(f+g*h)-i"
A = "q+(c*t)*o+(g*g)+q*(i-a)*p-(i*l)"
print(c.postfix(A))
