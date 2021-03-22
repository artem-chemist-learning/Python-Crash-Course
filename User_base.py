class User():
    
    def __init__(self, first = '', last='', active = True, rank = 1):
       self.first = first
       self.last=last
       self.active = active
       self.rank = rank
       
    def Describe(self):
        if self.active: 
            print('Full name:' + self.first.title() + " " + self.last.title() )
            print('Rank:' + str(self.rank))
        else:
            print('This user has been deactivated')
