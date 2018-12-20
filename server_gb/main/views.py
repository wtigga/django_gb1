from django.http import HttpResponse
from django.template.loader import get_template
import urllib.request, json


# Create your views here.
def usd_rub_rate():
    with urllib.request.urlopen(
            "http://free.currencyconverterapi.com/api/v5/convert?q=USD_RUB&compact=y") as url:
        data = round((json.load(url)['USD_RUB']["val"]),
                     3)  # get currency rate from VAL, round to 3 digits float
        output = (str(data))
    return output


def main_view(request):
    context = {
        'title': 'Главная страница',
        'subtitle': 'Подзаголовок страницы',
        'username': request.user,
        'currency_usd': usd_rub_rate(),
    }
    template = get_template('main/index.html')
    return HttpResponse(template.render(context))


def about_view(request):
    context = {
        'title': 'О сайте',
        'subtitle': 'Подзаголовок страницы',
        'username': request.user,
        'currency_usd': usd_rub_rate(),
    }
    template = get_template('main/about.html')
    return HttpResponse(template.render(context))


def contacts_view(request):
    context = {
        'title': 'О сайте',
        'subtitle': 'Подзаголовок страницы',
        'username': request.user,
        'currency_usd': usd_rub_rate(),
    }
    template = get_template('main/contacts.html')
    return HttpResponse(template.render(context))