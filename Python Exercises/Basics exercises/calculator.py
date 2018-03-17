def calculate():
    operation = input(
    '''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    #Addition
    if operation == '+':
        print('{} + {} = ' .format(number_1, number_2))
        print(number_1 + number_2)

    # #Subtraction
    elif operation == '-':
        print('{} - {} = ' .format(number_1, number_2))
        print(number_1 - number_2)

    # #Multiplication
    elif operation == '*':
        print('{} * {} = ' .format(number_1, number_2))
        print(number_1 * number_2)

    # #Division
    elif operation == '/':
        print('{} / {} = ' .format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not entered a valid operator, please run the program again.')

    def again():
        calc_again = input('''
        Do you want to make another calculation?
        Y for YES
        N for NO
        ''')

        if calc_again.upper() == 'Y':
            calculate()

        elif  calc_again.upper() == 'N':
            print('Have a wonderful day!')

        else:
            again()

    again()

calculate()