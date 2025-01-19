class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        peri = self.a + self.b + self.c
        return peri
sides = triangle(5, 8, 9)
perimeter = sides.perimeter()
print(perimeter)