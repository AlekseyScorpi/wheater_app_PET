import requests
from settings import API_KEY, LANGUAGE


def main():
    city_name = input('Введите название города: ')
    request = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}'
    response = requests.get(request)
    response = response.json()[0]
    request = f'https://api.openweathermap.org/data/2.5/weather?lat={response["lat"]}' \
              f'&lon={response["lon"]}&lang={LANGUAGE}&appid={API_KEY}&units=metric'
    response = requests.get(request).json()
    print(f'Текущая погода в {city_name}:')
    print(f'{response["weather"][0]["description"].capitalize()}')
    print(f'Температура воздуха: {response["main"]["temp"]} градусов по цельсию')
    print(f'Ощущается как: {response["main"]["feels_like"]} градусов по цельсию')
    print(f'Ветер {response["wind"]["speed"]} м/c')


if __name__ == '__main__':
    main()
