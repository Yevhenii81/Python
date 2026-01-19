import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import FortuneCookie, Poem, Author, Theme
from .serializers import (
    FortuneCookieSerializer,
    PoemSerializer,
    AuthorSerializer,
    ThemeSerializer
)

# ================== Главная ==================
def home(request):
    return HttpResponse("""
    <h1>hw_13_01 — REST API</h1>
    <ul>
        <li>/fortune/ — случайное предсказание</li>
        <li>/random/ — случайное число</li>
        <li>/random/10/50/ — число в диапазоне</li>
        <li>/random_set/5/?min=1&max=20 — набор чисел</li>
        <li>/poem/random/ — случайный стих</li>
        <li>/poem/author/1/ — стихи автора</li>
        <li>/poem/theme/2/ — стихи по теме</li>
        <li>/authors/ — все авторы</li>
        <li>/themes/ — все тематики</li>
    </ul>
    """)

# ================== Задание 1: Предсказания ==================
DEFAULT_FORTUNES = [
    "Сегодня вас ждёт приятная встреча.",
    "Удача будет сопровождать вас весь день.",
    "Скоро вы получите хорошие новости.",
    "Ваши старания обязательно принесут результат.",
    "Сегодня отличный день для новых начинаний."
]

@api_view(['GET'])
def fortune(request):
    cookies = list(FortuneCookie.objects.all())

    if cookies:
        cookie = random.choice(cookies)
        serializer = FortuneCookieSerializer(cookie)
        return Response(serializer.data)

    return Response({
        "fortune": random.choice(DEFAULT_FORTUNES)
    })


# ================== Задание 2: Случайные числа ==================
@api_view(['GET'])
def random_number(request):
    return Response({
        "number": random.randint(0, 100)
    })

@api_view(['GET'])
def random_number_range(request, min_value: int, max_value: int):
    return Response({
        "number": random.randint(min_value, max_value)
    })

@api_view(['GET'])
def random_number_set(request, count: int):
    min_val = int(request.GET.get('min', 0))
    max_val = int(request.GET.get('max', 100))

    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    return Response({
        "numbers": numbers
    })


# ================== Задание 3: Стихи ==================
DEFAULT_POEMS = [
    {
        "title": "Життя",
        "author": "Невідомий",
        "theme": "Життя",
        "text": "Життя — це мить між двома подихами.\nЦінуй її щодня."
    },
    {
        "title": "Кохання",
        "author": "Невідомий",
        "theme": "Любов",
        "text": "Кохання не питає дозволу,\nВоно просто приходить."
    }
]

@api_view(['GET'])
def poem_random(request):
    poems = list(Poem.objects.all())

    if poems:
        poem = random.choice(poems)
        serializer = PoemSerializer(poem)
        return Response(serializer.data)

    return Response(random.choice(DEFAULT_POEMS))


@api_view(['GET'])
def poem_by_author(request, author_id: int):
    poems = Poem.objects.filter(author_id=author_id)

    if poems.exists():
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    return Response({
        "author_id": author_id,
        "poems": [
            {
                "title": "Тиша",
                "text": "У тиші народжуються найглибші думки."
            }
        ]
    })


@api_view(['GET'])
def poem_by_theme(request, theme_id: int):
    poems = Poem.objects.filter(theme_id=theme_id)

    if poems.exists():
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    return Response({
        "theme_id": theme_id,
        "poems": [
            {
                "title": "Надія",
                "text": "Навіть у темряві зірка надії світить."
            }
        ]
    })


# ================== Задание 4: Доп. функционал ==================
@api_view(['GET'])
def all_authors(request):
    authors = Author.objects.all()

    if authors.exists():
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    return Response({
        "authors": ["Невідомий"]
    })


@api_view(['GET'])
def all_themes(request):
    themes = Theme.objects.all()

    if themes.exists():
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)

    return Response({
        "themes": ["Любов", "Життя", "Творчість"]
    })


@api_view(['GET'])
def poem_titles_by_theme(request, theme_id: int):
    poems = Poem.objects.filter(theme_id=theme_id)

    if poems.exists():
        return Response({
            "titles": [p.title for p in poems]
        })

    return Response({
        "titles": ["Надія", "Світло"]
    })


@api_view(['GET'])
def poem_titles_by_author(request, author_id: int):
    poems = Poem.objects.filter(author_id=author_id)

    if poems.exists():
        return Response({
            "titles": [p.title for p in poems]
        })

    return Response({
        "titles": ["Тиша", "Думки"]
    })
