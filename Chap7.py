toppings = []
NeedMoreToppings = True
while NeedMoreToppings:
    NextTopping = input('What topping would you like to add (None to finish):')
    if NextTopping !='None':
        toppings.append(NextTopping)
        print(NextTopping + 'will be added')
    else:
        NeedMoreToppings = False
        