# ================================================================
#                   HW 02.12 — OOP Python
#   ЧАСТИНА 1 • Множинне успадкування / Поліморфізм / Магічні методи
#   ЧАСТИНА 2 • Успадкування Device / Ship / Money / Product
# ================================================================

import json
import math

# ================================================================
#                         ЧАСТИНА 1
#            Множинне успадкування. Площа фігур
# ================================================================

class Figure:
    def area(self):
        raise NotImplementedError("Метод area() має бути перевизначений")

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Прямокутник {self.width}x{self.height}, площа = {self.area()}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Коло (R={self.radius}), площа = {self.area():.2f}"

class RightTriangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return (self.a * self.b) / 2

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Прямокутний трикутник {self.a}x{self.b}, площа = {self.area()}"

class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Трапеція ({self.a}, {self.b}, h={self.h}), площа = {self.area()}"

# Base class для Shape
class Shape:
    def show(self):
        raise NotImplementedError

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f, ensure_ascii=False)

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.__dict__.update(data)

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        return f"Квадрат: ({self.x},{self.y}), сторона {self.side}"

class RectShape(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self):
        return f"Прямокутник: ({self.x},{self.y}), {self.w}x{self.h}"

class CircleShape(Shape):
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def show(self):
        return f"Коло: центр ({self.cx},{self.cy}), R={self.r}"

class Ellipse(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self):
        return f"Еліпс: ({self.x},{self.y}), {self.w}x{self.h}"

# ================================================================
#                         ЧАСТИНА 2
#                       Успадкування
# ================================================================

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

class CoffeeMachine(Device):
    def make_coffee(self):
        return f"{self.info()} готує каву..."

class Blender(Device):
    def blend(self):
        return f"{self.info()} перемелює продукти..."

class MeatGrinder(Device):
    def grind(self):
        return f"{self.info()} перемелює м'ясо..."

class Ship:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def info(self):
        return f"{self.name} ({self.country})"

class Frigate(Ship):
    def attack(self):
        return f"{self.info()} атакує торпедами!"

class Destroyer(Ship):
    def attack(self):
        return f"{self.info()} запускає ракети!"

class Cruiser(Ship):
    def attack(self):
        return f"{self.info()} веде артилерійський вогонь!"

class Money:
    def __init__(self, units, coins):
        self.units = units
        self.coins = coins

    def set_value(self, units, coins):
        self.units = units
        self.coins = coins

    def display(self):
        return f"{self.units}.{str(self.coins).zfill(2)}"

class Product(Money):
    def __init__(self, name, units, coins):
        super().__init__(units, coins)
        self.name = name

    def discount(self, amount):
        total = self.units * 100 + self.coins
        total -= int(amount * 100)
        self.units = total // 100
        self.coins = total % 100

    def info(self):
        return f"{self.name}: {self.display()} грн"

# ================================================================
#                        ТЕСТ КЛАССОВ
# ================================================================

if __name__ == "__main__":
    print("\n══════════════ ЧАСТИНА 1 — Площі фігур ═════════════\n")
    f1 = Rectangle(10, 5)
    f2 = Circle(7)
    f3 = RightTriangle(3, 4)
    f4 = Trapezoid(5, 7, 4)

    for f in [f1, f2, f3, f4]:
        print(str(f))

    print("\n--- Shape Save/Load ---\n")
    shapes = [
        Square(0, 0, 10),
        RectShape(5, 5, 20, 10),
        CircleShape(10, 10, 7),
        Ellipse(2, 2, 15, 8)
    ]

    for i, s in enumerate(shapes):
        s.save(f"shape_{i}.json")

    loaded = []
    for i in range(4):
        obj = Square(0, 0, 1)
        obj.load(f"shape_{i}.json")
        loaded.append(obj)

    for s in loaded:
        print(s.show())

    print("\n══════════════ ЧАСТИНА 2 — Успадкування ═════════════\n")
    cm = CoffeeMachine("Philips", "X200")
    bl = Blender("Tefal", "BlendPro")
    mg = MeatGrinder("Bosch", "MG900")

    for dev in [cm, bl, mg]:
        if isinstance(dev, CoffeeMachine):
            print(dev.make_coffee())
        elif isinstance(dev, Blender):
            print(dev.blend())
        elif isinstance(dev, MeatGrinder):
            print(dev.grind())

    print()
    ships = [
        Frigate("Horizon", "UK"),
        Destroyer("Falcon", "USA"),
        Cruiser("Moskva", "RU")
    ]

    for s in ships:
        print(s.attack())

    print("\n--- MONEY / PRODUCT ---\n")
    p = Product("Чай", 50, 0)
    print(p.info())
    p.discount(5)
    print("Після знижки:", p.info())
