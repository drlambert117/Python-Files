import json

# my_pets = [['Molly', 'dog', 'large', 'friendly'], ['Kitty', 'cat', 'medium', 'antisocial'], ['Purry', 'cat', 'small', 'sweet'], ['Togepi', 'hedghog', 'tiny', 'timid']]

# my_pets = '{"pets":[{"name":"Molly","species":"dog","size":"large","personality":"friendly"},{"name":"Kitty","species":"cat","size":"medium","personality":"antisocial"},{"name":"Purry","species":"cat","size":"small","personality":"sweet"}]}'

my_pets = '[{"name":"Molly","species":"dog","size":"large","personality":"friendly"},{"name":"Kitty","species":"cat","size":"medium","personality":"antisocial"},{"name":"Purry","species":"cat","size":"small","personality":"sweet"}]'
pets = json.loads(my_pets)

for pet in pets:
    print(pet["name"] + ' is a ' + pet["size"] + ', ' +  pet["personality"] + ' ' + pet["species"])


# print('I have ' + str(len(pets)) + ' pets:')


# for i in range(len(pets)) :
#     print(pets[i][0] + ' is a ' + pets[i][2] + ', ' +  pets[i][3] + ' ' + pets[i][1])