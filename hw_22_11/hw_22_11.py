import random

# ===============================
# ЗАДАЧА 1
# ===============================
# Создание 5x5 массива
matrix1 = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]

print("===== ЗАДАЧА 1: Исходный массив =====")
for row in matrix1:
    print(row)

# Перестановка относительно главной диагонали
for i in range(5):
    for j in range(i + 1, 5):
        matrix1[i][j], matrix1[j][i] = matrix1[j][i], matrix1[i][j]

print("\n===== После перестановки относительно главной диагонали =====")
for row in matrix1:
    print(row)


# ===============================
# ЗАДАЧА 2
# ===============================
matrix2 = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]

print("\n===== ЗАДАЧА 2: Исходный массив =====")
for row in matrix2:
    print(row)

# Замена главной диагонали на побочную
for i in range(5):
    matrix2[i][i], matrix2[i][4 - i] = matrix2[i][4 - i], matrix2[i][i]

print("\n===== После замены диагоналей =====")
for row in matrix2:
    print(row)


# ===============================
# ЗАДАЧА 3
# ===============================
matrix3 = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]

print("\n===== ЗАДАЧА 3: Массив =====")
for row in matrix3:
    print(row)

# Превращение матрицы в одномерный список
flat = [x for row in matrix3 for x in row]

mn = min(flat)
mx = max(flat)

idx_min = flat.index(mn)
idx_max = flat.index(mx)

start = min(idx_min, idx_max) + 1
end = max(idx_min, idx_max)

summation = sum(flat[start:end])

print(f"\nМинимальный элемент: {mn} (индекс {idx_min})")
print(f"Максимальный элемент: {mx} (индекс {idx_max})")
print(f"Сумма элементов между ними: {summation}")
