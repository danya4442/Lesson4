from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(100,300)
        self.power = randint(20,80)

        Pokemon.pokemons[pokemon_trainer] = self



    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data ["sprites"]["other"]["official-artwork"]["front_shiny"])
        else:
            return "https://i.pinimg.com/736x/49/e5/63/49e5631e24fd43af0287e45d3322162c.jpg"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье покемона: {self.hp}
Сила покемона: {self.power}
"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



