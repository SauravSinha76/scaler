class Circle:
    # Define properties here
    radius =0
    pi = 3.14

    # Define constructor here
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.pi * self.radius

    # Complete the function

    def area(self):
        return self.pi * self.radius * self.radius
# Complete the function