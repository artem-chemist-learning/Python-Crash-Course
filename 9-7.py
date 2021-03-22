from User_base import User
from Privelege_class import Privelege

class Admin(User):
    def __init__(self, first, last, active, rank):
        super().__init__(first, last, active, rank)
        self.rank = 100
        self.priveleges = [
                Privelege('overwrite'), 
                Privelege('delete'),
                Privelege('ban'),
                ]
        
    def show_priveleges(self):
        for privelege in self.priveleges:
            privelege.identify()


Vasya = Admin('Vasiliy','Pupkin',True,1)
Vasya.show_priveleges()