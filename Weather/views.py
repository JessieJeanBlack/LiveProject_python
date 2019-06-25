from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?&units=imperial&appid=bf357a3c897f482670e76847febb1cb5'

    if request.method == 'POST':
        pass

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'icon' : ['icon'],
    }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data}
    return render(request, 'weather/weather.html', context)
