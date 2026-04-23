class Polygon:
    def area(self):
        pass


class Triangle(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3**0.5 / 4) * self.side * self.side


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * (3**0.5) / 2) * self.side * self.side


print("Choose shape:")
print("1. Triangle")
print("2. Rectangle")
print("3. Hexagon")

choice = int(input("Enter your choice: "))

if choice == 1:
    side = float(input("Enter side of triangle: "))
    shape = Triangle(side)

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)

elif choice == 3:
    side = float(input("Enter side of hexagon: "))
    shape = Hexagon(side)

else:
    print("Invalid choice")
    exit()

print("Area =", shape.area())