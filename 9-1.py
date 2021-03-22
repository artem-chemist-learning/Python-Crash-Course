class Restaurant():
    
    def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
    
    def describe(self):
        print('This restaurant is called {}'.format(self.name))
        print ('It serves {} food'.format(self.cuisine))
        
    def OpenTheDoors(self):
        print('Opening {}'.format(self.name))
        

WurstBar = Restaurant('Wurst bar', 'German')

WurstBar.describe()
LocalRestaurants = []

for i in range(3):
   LocalRestaurants.append(Restaurant(i,str(i) + 'sh'))

print(LocalRestaurants[0].name)