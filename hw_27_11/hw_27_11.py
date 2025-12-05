import time

# -------------------------------
#   PART 1 — Generators, HOF, Decorators
# -------------------------------

# ---------- Task 1 ----------
def odd_numbers(start, end):
    for n in range(start, end + 1):
        if n % 2 != 0:
            yield n


# ---------- Task 2 ----------
def values_outside_range(lst, start, end):
    for item in lst:
        if not (start <= item <= end):
            yield item


# ---------- Task 3 ----------
def horizontal_line(symbol):
    return symbol * 20


def vertical_line(symbol):
    return "\n".join(symbol for _ in range(10))


def show_line(symbol, function_to_call):
    print("\n--- Line Output ---")
    print(function_to_call(symbol))
    print("-------------------\n")


# ---------- Task 4 ----------
def measure_time(func):
    def wrapper(*args, **kwargs):
        print(f"\n=== Executing: {func.__name__} ===")
        start = time.time()
        result = list(func(*args, **kwargs))
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        print(f"Result sample (first 20 numbers): {result[:20]}")
        print(f"Total numbers: {len(result)}")
        print("=================================\n")
        return result
    return wrapper


@measure_time
def even_numbers_100k():
    for n in range(0, 100001):
        if n % 2 == 0:
            yield n


# ---------- Task 5 ----------
@measure_time
def even_numbers_range(start, end):
    for n in range(start, end + 1):
        if n % 2 == 0:
            yield n


# -------------------------------
#   PART 2 — Generators, HOF, Decorators
# -------------------------------

# ---------- Task 1 ----------
def fibonacci_range(start, end):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            yield a
        a, b = b, a + b


# ---------- Task 2 ----------
def sum_lists(list1, list2):
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        v1 = list1[i] if i < len(list1) else 0
        v2 = list2[i] if i < len(list2) else 0
        yield v1 + v2


# ---------- Task 3 ----------
def square(x): return x ** 2
def cube(x): return x ** 3

def calculate(list_to_work, function_to_call):
    return [function_to_call(x) for x in list_to_work]


# ---------- Task 4 ----------
def to_json(func):
    import json
    def wrapper():
        print("\n=== JSON Report ===")
        result = json.dumps(func(), indent=4)
        print(result)
        print("===================\n")
        return result
    return wrapper


def to_csv(func):
    import csv
    import io
    def wrapper():
        print("\n=== CSV Report ===")
        output = io.StringIO()
        writer = csv.writer(output)
        for row in func():
            writer.writerow(row)
        result = output.getvalue()
        print(result)
        print("===================\n")
        return result
    return wrapper


def generate_report():
    return [
        ["Department", "Amount"],
        ["Sales", 12000],
        ["Marketing", 5000],
        ["IT", 9000]
    ]


report_json = to_json(generate_report)
report_csv = to_csv(generate_report)


# -------------------------------
# Test runs (beautiful output)
# -------------------------------
if __name__ == "__main__":
    print("\n===== TASK 1: Odd numbers =====")
    print(list(odd_numbers(1, 20)))

    print("\n===== TASK 2: Values outside range =====")
    print(list(values_outside_range([1, 5, 10, 15], 3, 12)))

    print("\n===== TASK 3: Lines =====")
    show_line("*", horizontal_line)
    show_line("#", vertical_line)

    even_numbers_100k()                    # decorator already prints nicely
    even_numbers_range(10, 50)             # decorator prints nicely

    print("\n===== PART 2 — TASK 1: Fibonacci =====")
    print(list(fibonacci_range(0, 100)))

    print("\n===== PART 2 — TASK 2: Sum of two lists =====")
    print(list(sum_lists([1, 3, 4, 2], [8, 3, 5, 9])))

    print("\n===== PART 2 — TASK 3: Square/Cube =====")
    print("Squared:", calculate([1, 2, 3], square))
    print("Cubed:", calculate([1, 2, 3], cube))

    print("\n===== PART 2 — TASK 4: Reports =====")
    report_json()
    report_csv()
