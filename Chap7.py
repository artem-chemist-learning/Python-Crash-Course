GoOn= True
age = 0

def GetInput():
    UsrInput = input('How old are you (enough to finish)): ')
    if UsrInput.title() =='Enough':
        return False
    else:
        age = int(UsrInput)
        return True
        
while GetInput():
    if age<3:
        print('Your ticket is free')
    elif age<12:
        print('Your ticket is $10')
    elif age>12:
        print('Your ticket is $15')

        