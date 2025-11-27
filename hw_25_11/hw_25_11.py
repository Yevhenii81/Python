# ---------------------------------
# ЧАСТИНА 1 — КОРТЕЖІ / МНОЖИНИ
# ---------------------------------

def part1():
    print("===== ЧАСТИНА 1 =====")

    # Завдання 1
    print("\n--- Завдання 1 ---")
    t1 = (1, 2, 3, 4, 5)
    t2 = (3, 4, 5, 6, 7)
    t3 = (5, 4, 8, 9, 3)

    common = set(t1) & set(t2) & set(t3)
    print("Елементи у всіх кортежах:", common)

    # Завдання 2
    print("\n--- Завдання 2 ---")
    t1 = (1, 2, 3, 4)
    t2 = (3, 4, 5, 6)
    t3 = (4, 6, 7, 8)

    unique_t1 = set(t1) - set(t2) - set(t3)
    unique_t2 = set(t2) - set(t1) - set(t3)
    unique_t3 = set(t3) - set(t1) - set(t2)

    print("Унікальні t1:", unique_t1)
    print("Унікальні t2:", unique_t2)
    print("Унікальні t3:", unique_t3)

    # Завдання 3
    print("\n--- Завдання 3 ---")
    t1 = (1, 2, 3, 4, 5)
    t2 = (1, 9, 3, 7, 5)
    t3 = (1, 2, 3, 0, 5)

    same_pos = []
    for i in range(min(len(t1), len(t2), len(t3))):
        if t1[i] == t2[i] == t3[i]:
            same_pos.append((i, t1[i]))

    print("Елементи на тій самій позиції:", same_pos)


# ---------------------------------
# ЧАСТИНА 2 — СЛОВНИКИ
# ---------------------------------

def part2():
    print("\n===== ЧАСТИНА 2 =====")

    # -----------------------------
    # Завдання 1 — Баскетболісти
    # -----------------------------
    print("\n--- Завдання 1: Баскетболісти ---")
    players = {}

    def add_player(name, height):
        players[name] = height

    def delete_player(name):
        players.pop(name, None)

    def find_player(name):
        return players.get(name)

    def update_player(name, new_height):
        if name in players:
            players[name] = new_height

    add_player("Michael Jordan", 198)
    add_player("LeBron James", 206)
    update_player("LeBron James", 207)
    print(players)


    # -----------------------------
    # Завдання 2 — Англо-французький словник
    # -----------------------------
    print("\n--- Завдання 2: Англо-французький словник ---")
    dictionary = {}

    def add_word(en, fr):
        dictionary[en] = fr

    def delete_word(en):
        dictionary.pop(en, None)

    def find_word(en):
        return dictionary.get(en)

    def update_word(en, new_fr):
        if en in dictionary:
            dictionary[en] = new_fr

    add_word("apple", "pomme")
    add_word("cat", "chat")
    update_word("cat", "le chat")
    print(dictionary)


    # -----------------------------
    # Завдання 3 — Програма «Фірма»
    # -----------------------------
    print("\n--- Завдання 3: Фірма ---")
    company = {}

    def add_employee(name, phone, email, position, room, skype):
        company[name] = {
            "phone": phone,
            "email": email,
            "position": position,
            "room": room,
            "skype": skype
        }

    def delete_employee(name):
        company.pop(name, None)

    def find_employee(name):
        return company.get(name)

    def update_employee(name, field, value):
        if name in company and field in company[name]:
            company[name][field] = value

    add_employee("John Smith", "555-123", "john@corp.com", "Manager", 101, "john.smith")
    update_employee("John Smith", "room", 202)
    print(company)


    # -----------------------------
    # Завдання 4 — Книжкова колекція
    # -----------------------------
    print("\n--- Завдання 4: Книжкова колекція ---")
    books = {}

    def add_book(title, author, genre, year, pages, publisher):
        books[title] = {
            "author": author,
            "genre": genre,
            "year": year,
            "pages": pages,
            "publisher": publisher
        }

    def delete_book(title):
        books.pop(title, None)

    def find_book(title):
        return books.get(title)

    def update_book(title, field, value):
        if title in books and field in books[title]:
            books[title][field] = value

    add_book("1984", "George Orwell", "Dystopia", 1949, 328, "Secker & Warburg")
    update_book("1984", "pages", 330)
    print(books)


# Запуск частин
if __name__ == "__main__":
    part1()
    part2()
