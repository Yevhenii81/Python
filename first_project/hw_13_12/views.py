from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Данные
cities_data = {
    "paris": {1924: "Олимпийские игры в Париже"},
    "marseille": {1956: "Развитие порта"}
}

history_data = {
    1885: "Франция в эпоху колониализма",
    1914: "Первая мировая война"
}


def home(request):
    return HttpResponse("<h1>Франция</h1>")


def history(request):
    return HttpResponse("<h1>История Франции</h1>")


def cities(request):
    city = request.GET.get("city")
    year = request.GET.get("year")

    if city and year:
        return city_year(request, city.lower(), int(year))

    return HttpResponse("<h1>Города Франции</h1>")


def facts(request):
    return HttpResponse("<h1>Факты о Франции</h1>")


def city_detail(request, city):
    city = city.lower()
    if city in cities_data:
        return HttpResponse(f"<h1>{city.title()}</h1>")
    return HttpResponseRedirect(reverse('cities'))


def city_year(request, city, year):
    city = city.lower()
    if city in cities_data and year in cities_data[city]:
        return HttpResponse(f"<h1>{city.title()} {year}</h1><p>{cities_data[city][year]}</p>")
    return HttpResponseRedirect(reverse('cities'))


def history_year(request, year):
    if year in history_data:
        return HttpResponse(f"<h1>{year}</h1><p>{history_data[year]}</p>")
    return HttpResponseRedirect(reverse('history'))
