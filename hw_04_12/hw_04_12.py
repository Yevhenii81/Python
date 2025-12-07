# ================================================================
#              HW — ООП + ФАЙЛИ (Перевантаження операторів)
# ================================================================

import os

# ================================================================
#                      ЧАСТИНА 1 — ООП
# ================================================================
# ---------------------------- ЗАВДАННЯ 1 -------------------------
#                          Клас Circle
# ================================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # == (радіуси)
    def __eq__(self, other):
        return self.radius == other.radius

    # Порівняння довжин кіл
    def length(self):
        return 2 * 3.14159 * self.radius

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    # Пропорційна зміна радіуса (+ і -)
    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __str__(self):
        return f"Коло (R = {self.radius})"


# ================================================================
#                       ЗАВДАННЯ 2 — Complex
# ================================================================

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # +  
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # -
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # *
    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    # /
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom
        )

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# ================================================================
#                       ЗАВДАННЯ 3 — Airplane
# ================================================================

class Airplane:
    def __init__(self, plane_type, passengers, max_passengers):
        self.plane_type = plane_type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    # + і - (зміна кількості пасажирів)
    def __add__(self, value):
        return Airplane(self.plane_type, self.passengers + value, self.max_passengers)

    def __sub__(self, value):
        return Airplane(self.plane_type, self.passengers - value, self.max_passengers)

    def __iadd__(self, value):
        self.passengers += value
        return self

    def __isub__(self, value):
        self.passengers -= value
        return self

    # Порівняння за max_passengers
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __str__(self):
        return f"{self.plane_type}: {self.passengers}/{self.max_passengers} пас."


# ================================================================
#                     ЗАВДАННЯ 4 — Flat
# ================================================================

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"Квартира: {self.area} м², {self.price}$"


# ================================================================
#                 ЧАСТИНА 2 — РОБОТА З ФАЙЛАМИ
# ================================================================

# ---------------------- Завдання 1 ------------------------------

def replace_python_with_java():
    if not os.path.exists("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write("Python is great.\nPython is powerful.")

    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read().replace("Python", "Java")

    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(text)


# ---------------------- Завдання 2 ------------------------------

def count_chars_per_line():
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("char_count.txt", "w", encoding="utf-8") as f:
        for i, line in enumerate(lines, 1):
            f.write(f"Рядок {i}: {len(line.strip())} символів\n")


# ---------------------- Завдання 3 ------------------------------

def compare_two_files():
    open("old_version.txt", "a").close()
    open("new_version.txt", "a").close()

    with open("old_version.txt", "r", encoding="utf-8") as f1:
        old = set(f1.readlines())

    with open("new_version.txt", "r", encoding="utf-8") as f2:
        new = set(f2.readlines())

    diff = old.symmetric_difference(new)

    with open("differences.txt", "w", encoding="utf-8") as out:
        out.writelines(diff)


# ---------------------- Завдання 4 ------------------------------

def censor_words():
    open("source.txt", "a").close()
    open("words.txt", "a").close()

    with open("source.txt", "r", encoding="utf-8") as f:
        text = f.read()

    with open("words.txt", "r", encoding="utf-8") as f:
        bad = [w.strip() for w in f.readlines()]

    for word in bad:
        text = text.replace(word, "***")

    with open("censored.txt", "w", encoding="utf-8") as f:
        f.write(text)


# ================================================================
#             ЗАВДАННЯ 5 — МЕНЮ orders.txt
# ================================================================

def orders_menu():
    filename = "orders.txt"
    open(filename, "a").close()

    while True:
        print("\n--- МЕНЮ ЗАМОВЛЕНЬ ---")
        print("1. Додати замовлення")
        print("2. Переглянути всі")
        print("3. Пошук")
        print("4. Оновити")
        print("5. Видалити")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            num = input("Номер: ")
            item = input("Товар: ")
            qty = input("Кількість: ")
            price = input("Ціна: ")
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{num};{item};{qty};{price}\n")

        elif choice == "2":
            with open(filename, "r", encoding="utf-8") as f:
                print(f.read() or "Файл порожній.")

        elif choice == "3":
            num = input("Введіть номер: ")
            with open(filename, "r", encoding="utf-8") as f:
                found = False
                for line in f:
                    if line.startswith(num + ";"):
                        print(line.strip())
                        found = True
                if not found:
                    print("Не знайдено.")

        elif choice == "4":
            num = input("Номер замовлення: ")
            updated = []
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for line in lines:
                if line.startswith(num + ";"):
                    item = input("Товар: ")
                    qty = input("Кількість: ")
                    price = input("Ціна: ")
                    updated.append(f"{num};{item};{qty};{price}\n")
                else:
                    updated.append(line)

            with open(filename, "w", encoding="utf-8") as f:
                f.writelines(updated)

        elif choice == "5":
            num = input("Номер: ")
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(filename, "w", encoding="utf-8") as f:
                for line in lines:
                    if not line.startswith(num + ";"):
                        f.write(line)

        elif choice == "6":
            break


# ================================================================
#            ЗАВДАННЯ 6 — МЕНЮ students.txt
# ================================================================

def students_menu():
    filename = "students.txt"
    open(filename, "a").close()

    while True:
        print("\n--- МЕНЮ СТУДЕНТІВ ---")
        print("1. Додати")
        print("2. Переглянути всі")
        print("3. Пошук")
        print("4. Оновити")
        print("5. Видалити")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Ім'я: ")
            course = input("Курс: ")
            avg = input("Середній бал: ")
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{name};{course};{avg}\n")

        elif choice == "2":
            with open(filename, "r", encoding="utf-8") as f:
                print(f.read() or "Порожньо.")

        elif choice == "3":
            name = input("Ім'я студента: ")
            with open(filename, "r", encoding="utf-8") as f:
                found = False
                for line in f:
                    if line.startswith(name + ";"):
                        print(line.strip())
                        found = True
                if not found:
                    print("Не знайдено.")

        elif choice == "4":
            name = input("Ім'я студента: ")
            updated = []
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for line in lines:
                if line.startswith(name + ";"):
                    course = input("Новий курс: ")
                    avg = input("Новий середній бал: ")
                    updated.append(f"{name};{course};{avg}\n")
                else:
                    updated.append(line)

            with open(filename, "w", encoding="utf-8") as f:
                f.writelines(updated)

        elif choice == "5":
            name = input("Ім'я: ")
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(filename, "w", encoding="utf-8") as f:
                for line in lines:
                    if not line.startswith(name + ";"):
                        f.write(line)

        elif choice == "6":
            break


# ================================================================
#                        ТЕСТИ ООП
# ================================================================

if __name__ == "__main__":
    print("\n══════════════ ТЕСТИ ООП ══════════════")

    # CIRCLE
    c1 = Circle(10)
    c2 = Circle(12)
    print("\n--- Circle ---")
    print(c1, c2)
    print("c1 == c2:", c1 == c2)
    print("c1 < c2:", c1 < c2)
    c1 += 5
    print("c1 після +=5:", c1)

    # COMPLEX
    print("\n--- Complex ---")
    a = Complex(3, 4)
    b = Complex(1, 2)
    print("a + b =", a + b)
    print("a * b =", a * b)

    # AIRPLANE
    print("\n--- Airplane ---")
    p1 = Airplane("Boeing", 100, 250)
    p2 = Airplane("Boeing", 80, 300)
    print("p1 == p2:", p1 == p2)
    print("p1 < p2:", p1 < p2)

    # FLAT
    print("\n--- Flat ---")
    f1 = Flat(50, 50000)
    f2 = Flat(60, 60000)
    print("f1 == f2:", f1 == f2)
    print("f1 < f2 (price):", f1 < f2)