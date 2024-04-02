class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * Circle.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius):
        return radius > 0


circle = Circle.from_diameter(10)
print("Радіус круга:", circle.radius)
print("Площа круга:", circle.calculate_area())
print("Довжина окружності круга:", circle.calculate_circumference())

print("Перевірка радіусу 5:", Circle.check_radius(5))
print("Перевірка радіусу -1:", Circle.check_radius(-1))
