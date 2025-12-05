# ============================================
#   HW 29.11 — OOP
# ============================================

print("\n========== ЧАСТИНА 1 — Класи. Об’єкти ==========\n")

# --------------------------------------------
#  Завдання 1 — Клас Автомобіль
# --------------------------------------------
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель: ")
        self.year = int(input("Рік випуску: "))
        self.manufacturer = input("Виробник: ")
        self.engine = float(input("Об’єм двигуна: "))
        self.color = input("Колір: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"\nАвтомобіль: {self.model}")
        print(f"Рік: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Двигун: {self.engine} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} $")

    def change_color(self, new_color):
        self.color = new_color


# --------------------------------------------
#  Завдання 2 — Клас Книга
# --------------------------------------------
class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Назва: ")
        self.year = int(input("Рік видання: "))
        self.publisher = input("Видавництво: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"\nКнига: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік: {self.year}")
        print(f"Видавництво: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Ціна: {self.price} грн")


# --------------------------------------------
#  Завдання 3 — Клас Стадіон
# --------------------------------------------
class Stadium:
    def __init__(self, name="", opened="", country="", city="", capacity=0):
        self.name = name
        self.opened = opened
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Назва: ")
        self.opened = input("Дата відкриття: ")
        self.country = input("Країна: ")
        self.city = input("Місто: ")
        self.capacity = int(input("Місткість: "))

    def display(self):
        print(f"\nСтадіон: {self.name}")
        print(f"Дата відкриття: {self.opened}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} осіб")


print("\n========== ЧАСТИНА 2 — Конструктори. Перевантаження ==========\n")

class Car(Car):
    @classmethod
    def from_string(cls, data):
        model, year, manufacturer, engine, color, price = data.split(",")
        return cls(model, int(year), manufacturer, float(engine), color, float(price))

    def __str__(self):
        return f"Car({self.model}, {self.year}, {self.manufacturer}, {self.engine}L, {self.color}, {self.price}$)"


class Book(Book):
    @classmethod
    def from_string(cls, data):
        title, year, publisher, genre, author, price = data.split(",")
        return cls(title, int(year), publisher, genre, author, float(price))

    def __str__(self):
        return f"Book({self.title}, {self.author}, {self.year})"


class Stadium(Stadium):
    @classmethod
    def from_string(cls, data):
        name, opened, country, city, capacity = data.split(",")
        return cls(name, opened, country, city, int(capacity))

    def __str__(self):
        return f"Stadium({self.name}, {self.city}, {self.capacity})"


print("\n========== ЧАСТИНА 3 — Статичні методи ==========\n")

# --------------------------------------------
#  Завдання 1 — Клас Дріб + статичний лічильник
# --------------------------------------------

class Fraction:
    _count = 0

    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        Fraction._count += 1

    @staticmethod
    def created_objects():
        return Fraction._count


# --------------------------------------------
#  Завдання 2 — Конвертер температур
# --------------------------------------------

class TemperatureConverter:
    _operations = 0

    @staticmethod
    def c_to_f(c):
        TemperatureConverter._operations += 1
        return c * 9/5 + 32

    @staticmethod
    def f_to_c(f):
        TemperatureConverter._operations += 1
        return (f - 32) * 5/9

    @staticmethod
    def total_operations():
        return TemperatureConverter._operations


# --------------------------------------------
#  Завдання 3 — Конвертер метрична <-> англійська
# --------------------------------------------

class LengthConverter:
    # 1 метр = 3.28084 фута
    @staticmethod
    def meters_to_feet(m):
        return m * 3.28084

    @staticmethod
    def feet_to_meters(f):
        return f / 3.28084


# --------------------------------------------
#  ТЕСТОВІ ВИВОДИ
# --------------------------------------------

if __name__ == "__main__":
    print("\n--- ТЕСТ КЛАСІВ ---")

    car = Car("BMW M5", 2020, "BMW", 4.4, "Black", 90000)
    print(car)

    book = Book.from_string("IT,2020,Kyiv,Education,John Smith,500")
    print(book)

    stadium = Stadium("Camp Nou", "1957", "Spain", "Barcelona", 99354)
    print(stadium)

    print("\n--- ДРІБ ---")
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print("Кількість створених дробів:", Fraction.created_objects())

    print("\n--- ТЕМПЕРАТУРА ---")
    print("20°C =", TemperatureConverter.c_to_f(20), "F")
    print("100°F =", TemperatureConverter.f_to_c(100), "C")
    print("К-сть операцій:", TemperatureConverter.total_operations())

    print("\n--- ДОВЖИНА ---")
    print("10 метрів =", LengthConverter.meters_to_feet(10), "футів")
    print("30 футів =", LengthConverter.feet_to_meters(30), "метрів")
