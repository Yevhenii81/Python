from django.http import HttpResponse
from datetime import datetime, timedelta

def menu():
    return """
    <nav>
        <a href="/">Головна</a> |
        <a href="/news/">Новини</a> |
        <a href="/datetime/">Дата і час</a> |
        <a href="/table/">Таблиця множення</a> |
        <a href="/programmer-day/">День програміста</a>
    </nav>
    <hr>
    """

def home(request):
    return HttpResponse(menu() + "<h1>Головна сторінка</h1>")

def news(request):
    return HttpResponse(menu() + "<h1>Новини</h1>")

def current_datetime(request):
    now = datetime.now()
    return HttpResponse(menu() + f"<h1>Поточна дата і час</h1><p>{now}</p>")

def multiplication_table(request):
    html = menu() + "<h1>Таблиця множення</h1><table border='1'>"
    for i in range(1, 11):
        html += "<tr>"
        for j in range(1, 11):
            html += f"<td>{i*j}</td>"
        html += "</tr>"
    html += "</table>"
    return HttpResponse(html)

def programmers_day(request):
    year = datetime.now().year
    day = datetime(year, 1, 1) + timedelta(days=255)
    return HttpResponse(menu() + f"<h1>День програміста {year}</h1><p>{day.date()}</p>")
