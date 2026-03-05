import requests
import os


API = os.getenv("WEATHER_API")
LAT = "55.71"
LON = "60.55"
LANG = "ru"
UNIT = "metric"
W_URL = (
    f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&'
    f'lon={LON}&appid={API}&lang={LANG}&units={UNIT}'
    )


class WeatherRequest():
    def __init__(self, api, url):
        self.api = api
        self.url = url

    def send_request(self):
        responce = requests.post(self.url)
        self.data = responce.json()

    def formated_responce(self):
        final = (
            f'В Кыштыме сейчас:\n'
            f'Погода: {self.data["weather"][0]["description"]}\n'
            f'Температура: {round(self.data["main"]["temp"])}\n'
            f'Влажность: {self.data["main"]["humidity"]}%\n'
            f'Давление: {self.data["main"]["pressure"]} Гпа'
        )
        return final


if __name__ == "__main__":
    weather_in_kyshtym = WeatherRequest(API, W_URL)
    weather_in_kyshtym.send_request()
    print(weather_in_kyshtym.formated_responce())