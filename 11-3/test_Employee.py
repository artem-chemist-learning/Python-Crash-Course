from Employee_module import Employee
import unittest

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.Bob = Employee('Bob','Wolfanegl',100000)
        self.payraise = 10000
    
    def test_default_raise(self):
        self.Bob.giveRaise()
        self.assertEqual(105000, self.Bob.pay)
        
    def test_raise(self):
        self.Bob.giveRaise(self.payraise)
        self.assertEqual(110000, self.Bob.pay)
        
unittest.main()