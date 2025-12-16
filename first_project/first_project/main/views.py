from django.http import HttpResponse
from datetime import datetime, timedelta


def current_datetime(request):
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return HttpResponse(
        f"<h1>Поточна дата та час</h1><p>{now}</p>"
    )


def multiplication_table(request):
    html = "<h1>Таблиця множення (1–10)</h1>"
    html += "<table border='1' cellpadding='5'>"

    for i in range(1, 11):
        html += "<tr>"
        for j in range(1, 11):
            html += f"<td>{i} × {j} = {i*j}</td>"
        html += "</tr>"

    html += "</table>"
    return HttpResponse(html)


def programmers_day(request):
    year = datetime.now().year
    programmers_date = datetime(year, 1, 1) + timedelta(days=255)

    return HttpResponse(
        f"<h1>День програміста</h1>"
        f"<p>{programmers_date.strftime('%d.%m.%Y')}</p>"
    )
