import requests
add_pokemon_responce = requests.post('https://pokemonbattle.me:9104/pokemons',  headers = {'Content-Type' : 'application/json', "trainer_token": "48cfaa92e624d8dabe06401827df9885"},
json = {
    "name": "Бука",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})
print(add_pokemon_responce.text)

add_pokemon_responce = requests.put('https://pokemonbattle.me:9104/pokemons', 
headers = {'Content-Type' : 'application/json', "trainer_token": "48cfaa92e624d8dabe06401827df9885"},
json = {
    "pokemon_id": "21003",
    "name": "Пикачу"
})
print(add_pokemon_responce.text)

add_pokemon_responce = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
headers = {'Content-Type' : 'application/json', "trainer_token": "48cfaa92e624d8dabe06401827df9885"},
json = {
    "pokemon_id": "21003",
})
print(add_pokemon_responce.text)
