import requests


BASE_URL = "https://rickandmortyapi.com/api"


class RickAndMortyClient():
    def __init__(self, url):
        self.url = url

    def find_character(self, id): # max 826
        character_url = self.url + f"/character/{str(id)}"
        responce = requests.get(character_url)
        data = responce.json()
        info = (
            f"--Character is found--\n"
            f"ID: {data['id']}\n"
            f"Name: {data['name']}\n"
            f"Status: {data['status']}\n"
            f"Species: {data['species']}\n"
            f"Gender: {data['gender']}\n"
            f"Origin: {data['origin']['name']}"
        )
        print(info)

    def find_location(self, id): # max 126
        location_url = self.url + f"/location/{str(id)}"
        responce = requests.get(location_url)
        data = responce.json()
        info = (
            f"--Location is found--\n"
            f"ID: {data['id']}\n"
            f"Name: {data['name']}\n"
            f"Type: {data['type']}\n"
            f"Dimension: {data['dimension']}"
        )
        print(info)

    def find_episode(self, id): # max 51
        episode_url = self.url + f"/episode/{str(id)}"
        responce = requests.get(episode_url)
        data = responce.json()
        info = (
            f"--Episode is found--\n"
            f"ID: {data['id']}\n"
            f"Name: {data['name']}\n"
            f"Air Date: {data['air_date']}\n"
            f"Episode: {data['episode']}"
        )
        print(info)

if __name__ == "__main__":
    finder = RickAndMortyClient(BASE_URL)
    finder.find_character(67)
    finder.find_location(67)
    finder.find_episode(7)

