from django.shortcuts import render
from datetime import date

# ===== ГЛАВНАЯ =====
def home(request):
    return render(request, 'home.html')


# ===== ЗАДАНИЕ 1: ВХОД =====
def login_view(request):
    message = ''

    users = {
        'admin': ('admin123', 'Адміністратор'),
        'user': ('user123', 'Користувач'),
    }

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        if login in users and users[login][0] == password:
            message = f"Вітаємо! Рівень доступу: {users[login][1]}"
        else:
            message = "Неправильний логін або пароль"

    return render(request, 'login.html', {'message': message})


# ===== ЗАДАНИЕ 2: КАЛЬКУЛЯТОР =====
def calc_view(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            numbers = list(map(float, request.POST['numbers'].split()))
            if len(numbers) != 3:
                raise ValueError

            action = request.POST['action']

            if action == 'min':
                result = min(numbers)
            elif action == 'max':
                result = max(numbers)
            else:
                result = sum(numbers) / 3

        except:
            error = 'Введіть рівно три числа'

    return render(request, 'calc.html', {
        'result': result,
        'error': error
    })


# ===== ЗАДАНИЕ 3: РЕГИСТРАЦИЯ =====
def register_view(request):
    data = None

    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'age': request.POST.get('age'),
            'email': request.POST.get('email'),
            'gender': request.POST.get('gender'),
            'address': request.POST.get('address'),
            'news': 'Так' if request.POST.get('news') else 'Ні'
        }

    return render(request, 'register.html', {'data': data})


# ===== ЗАДАНИЕ 4: ДЕНЬ ПРОГРАММИСТА =====
def programmer_day(request):
    result = None

    days = [
        'понеділок', 'вівторок', 'середа',
        'четвер', 'пʼятниця', 'субота', 'неділя'
    ]

    months = [
        'січня', 'лютого', 'березня', 'квітня',
        'травня', 'червня', 'липня', 'серпня',
        'вересня', 'жовтня', 'листопада', 'грудня'
    ]

    if request.method == 'POST':
        year = int(request.POST['year'])
        is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        day = date(year, 9, 12 if is_leap else 13)

        result = f"{day.day} {months[day.month - 1]} ({days[day.weekday()]})"

    return render(request, 'day.html', {'result': result})
