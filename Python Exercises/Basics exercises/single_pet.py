import json

my_pet = '{"name": "Molly","species": "dog", "size": "large", "personality": "friendly"}'

pet = json.loads(my_pet)

print(pet["name"] + ' is a ' + pet["size"] + ', ' +  pet["personality"] + ' ' + pet["species"])