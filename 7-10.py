GoOn = True
Dreams = {}
while GoOn:
    name = input('What is your name? ')
    place = input('What is your dream vacation spot? ')
    Dreams[name.title()]=place.title()
    GoOn = input('Anyone else? (y/n)').lower() == 'y'