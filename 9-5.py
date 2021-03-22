class User():
    
    def __init__(self, first = '', last='', active = True, rank = 1):
       self.first = first
       self.last=last
       self.active = active
       self.rank = rank
       self.login_attempt = 0
       
    def Describe(self):
        if self.active: 
            print('Full name:' + self.first.title() + " " + self.last.title() )
            print('Rank:' + str(self.rank))
        else:
            print('This user has been deactivated')
    
    def increment_logins(self):
        self.login_attempt +=1
    
    def reset_logins(self):
        self.login_attempt = 0
        
    def login(self):
        self.increment_logins()
        print('This is your attempt# '+str(self.login_attempt))
            
user = User();
user.active = False
user.Describe()
            
for i in range(3):
    user.login()