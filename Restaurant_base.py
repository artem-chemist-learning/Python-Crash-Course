class Restaurant():
    
    def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
            self.number_served = 0
    
    def describe(self):
        print('This restaurant is called {}'.format(self.name))
        print ('It serves {} food'.format(self.cuisine))
        
    def OpenTheDoors(self):
        print('Opening {}'.format(self.name))
    
    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served (self, increment):
        self.number_served+=increment
