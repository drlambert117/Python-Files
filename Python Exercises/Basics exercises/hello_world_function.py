#This program says hello and asks for user's name and age
def hello():
    print('Hello World!')

    print('What is your name?')
    myName = input()

    print(f"It is good to meet you, {myName}")
    print('The length of your name is: ')
    print(len(myName))

    print('What is your age?')
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')

hello()