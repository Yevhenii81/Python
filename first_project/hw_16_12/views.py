from django.shortcuts import render, redirect
from datetime import datetime


# ===== Задание 1–2: Песня =====
def song_en(request):
    return render(request, 'hw_16_12/song.html', {
        'text': "We are the champions, my friends\n"
                "And we'll keep on fighting till the end.\n"
                "Queen, We are the champions",
        'author': "Queen"
    })

def song_fr(request):
    return render(request, 'hw_16_12/song.html', {
        'text': "Nous sommes les champions, mes amis\n"
                "Et nous continuerons à nous battre jusqu'à la fin\n"
                "Queen, nous sommes les champions",
        'author': "Queen"
    })

def song_de(request):
    return render(request, 'hw_16_12/song.html', {
        'text': "Wir sind die Champions, meine Freunde\n"
                "Und wir werden weiterkämpfen bis zum Ende\n"
                "Queen, wir sind die Champions",
        'author': "Queen"
    })

def song_es(request):
    return render(request, 'hw_16_12/song.html', {
        'text': "Somos los campeones, amigos míos\n"
                "Y seguiremos luchando hasta el final\n"
                "Queen, somos los campeones",
        'author': "Queen"
    })


# ===== Задание 3: Автомобили =====
def cars_home(request):
    return render(request, 'hw_16_12/cars.html', {'brand': 'Главная'})

def toyota(request):
    return render(request, 'hw_16_12/cars.html', {'brand': 'Toyota'})

def honda(request):
    return render(request, 'hw_16_12/cars.html', {'brand': 'Honda'})

def renault(request):
    return render(request, 'hw_16_12/cars.html', {'brand': 'Renault'})


# ===== Задание 4: День недели =====
def day_of_week(request):
    days = [
        'Понеділок',
        'Вівторок',
        'Середа',
        'Четвер',
        "Пʼятниця",
        'Субота',
        'Неділя'
    ]

    today_index = datetime.now().weekday()

    return render(request, 'hw_16_12/day.html', {
        'day': days[today_index],
        'bg_color': [
            '#e3f2fd',
            '#fce4ec',
            '#e8f5e9',
            '#fffde7',
            '#ede7f6',
            '#fbe9e7',
            '#e0f2f1',
        ][today_index]
    })


# ===== Задание 5: Наушники =====
def headphones(request):
    model = request.GET.get('model')

    data = {
        'budslive': "Samsung Galaxy Buds Live\n"
                    "Тип: внутриканальные\n"
                    "Время работы: до 6 часов\n"
                    "Активное шумоподавление: есть",
        'airpods': "Apple AirPods\n"
                   "Тип: внутриканальные\n"
                   "Время работы: до 5 часов\n"
                   "Активное шумоподавление: да"
    }

    return render(request, 'hw_16_12/headphones.html', {
        'info': data.get(model, 'Модель не знайдена')
    })
