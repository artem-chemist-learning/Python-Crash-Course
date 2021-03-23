usr_sum = 0
while True:
    number = input('Enter a number (q to quit): ')
    if number =='q':
        break
    try: 
        usr_int  =int(number)
    except ValueError:
        print('Whole numbers only, please')
    else:
        usr_sum+=usr_int
        print('Sum so far: {}'.format(usr_sum))
