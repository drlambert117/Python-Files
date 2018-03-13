import json

my_pets = '[{"name":"Molly","species":"dog","size":"large","personality":"friendly"},{"name":"Kitty","species":"cat","size":"medium","personality":"antisocial"},{"name":"Purry","species":"cat","size":"small","personality":"sweet"}]'
pets = json.loads(my_pets)

for pet in pets:
    print(pet["name"] + ' is a ' + pet["size"] + ', ' +  pet["personality"] + ' ' + pet["species"])