class Fraction:
    numrator = 0
    denominator =0
    # Define constructor here

    def __init__(self, *args):
        if len(args) >= 1:
            self.numrator = args[0]
        if len(args) >= 2:
            self.denominator = args[1]

    def gcd(self,a,b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
    def lowest_order(self,a):
        g = self.gcd(a.numrator,a.denominator)
        if g < 0:
            g *= -1

        a.numrator //= g
        a.denominator //= g

        return a

    def add(self, a):
        result = Fraction()
        result.denominator = self.denominator * a.denominator
        result.numrator = self.numrator * a.denominator + self.denominator * a.numrator
        return self.lowest_order(result)


    # Complete the function

    def subtract(self, a):
        result = Fraction()
        result.denominator = self.denominator * a.denominator
        result.numrator = self.numrator * a.denominator - self.denominator * a.numrator
        return self.lowest_order(result)

    # Complete the function

    def multiply(self, a):
        result = Fraction()
        result.denominator = self.denominator * a.denominator
        result.numrator = self.numrator * a.numrator
        return self.lowest_order(result)


# Complete the function

f1 = Fraction(1,3)
f2 = Fraction(9,16)
r1 = f1.add(f2)
print(r1.numrator)
print(r1.denominator)