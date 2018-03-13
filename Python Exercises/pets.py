my_pets = [['Molly', 'dog', 'large', 'friendly'], ['Kitty', 'cat', 'medium', 'antisocial'], ['Purry', 'cat', 'small', 'sweet'], ['Togepi', 'hedghog', 'tiny', 'timid']]

print('I have ' + str(len(my_pets)) + ' pets:')

for i in range(len(my_pets)) :
    print(my_pets[i][0] + ' is a ' + my_pets[i][2] + ', ' +  my_pets[i][3] + ' ' + my_pets[i][1])