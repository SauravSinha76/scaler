class ComplexNumber:
    real = 0
    imaginary = 0

    # Define constructor here
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, x: "ComplexNumber") -> "ComplexNumber":
        sum = ComplexNumber
        sum.real = self.real + x.real
        sum.imaginary = self.imaginary + x.imaginary
        return sum


    def subtract(self, x: "ComplexNumber") -> "ComplexNumber":

        diff = ComplexNumber
        diff.real = self.real - x.real
        diff.imaginary = self.imaginary - x.imaginary
        return diff

    def multiply(self, x: "ComplexNumber") -> "ComplexNumber":
        product = ComplexNumber
        product.real = self.real * x.real - self.imaginary * x.imaginary
        product.imaginary = self.imaginary * x.real + self.real * x.imaginary
        return product

    def divide(self, x: "ComplexNumber") -> "ComplexNumber":
        result = ComplexNumber
        denom = x.real * x.real + x.imaginary * x.imaginary
        result.real = (self.real * x.real + self.imaginary * x.imaginary)/denom
        result.imaginary = (self.imaginary * x.real - self.real * x.imaginary)/denom
        return result


a = ComplexNumber(10, 5)
b = ComplexNumber(2, 3)
c1 = a.add(b)
print(c1.real)
print(c1.imaginary)
# ComplexNumber c2 = a.subtract(b)
# ComplexNumber c3 = a.multiply(b)
# ComplexNumber c4 = a.divide(b)