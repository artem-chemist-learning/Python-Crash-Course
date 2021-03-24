class Employee:
    def __init__(self, first='', last='', pay=0):
            self.first = first
            self.last = last
            self.pay = pay
    
    def giveRaise(self, amount =5000):
        self.pay+=amount