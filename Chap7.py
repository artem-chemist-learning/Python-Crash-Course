GoOn= True
age = 0
while GoOn:
    UsrInput = input('How old are you (enough to finish)): ')
    if UsrInput.title() !='Enough':
        age = int(UsrInput)
    else:
        GoOn = False
        break
    if age<3:
        print('Your ticket is free')
    elif age<12:
        print('Your ticket is $10')
    elif age>12:
        print('Your ticket is $15')

        