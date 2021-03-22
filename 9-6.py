from Restaurant_base import Restaurant

class IceCreamStand (Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Vanilla','Chocolate','Banana']
    
    def sell_cone(self):
        print('Here is your cone')
        
a = IceCreamStand('Joes', 'American')

for flavor in a.flavors:
    print(flavor)
