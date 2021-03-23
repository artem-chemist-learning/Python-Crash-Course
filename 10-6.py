number_1 = input('First number: ')
number_2 = input('Second number: ')
int_1 = int_2 = 0
try: 
    int_1  =int(number_1)
except ValueError:
    print('Whole numbers only, please')
try: 
    int_2  =int(number_2)
except ValueError:
    print('Whole numbers only, please')

print('\n'+'The sum is '+str(int_1+int_2))
            