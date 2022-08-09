#pip install unittest2
import unittest
import sys, os, inspect

#get acces to the current directory and the parent directory in order to import modules from it
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)

from my_class import Square

#create class that inherits from the class unittest.TestCase
#Tests are written as methods of the class
class TestClass(unittest.TestCase):

    def test_area(self):
        #testing the method Square.area()

        sq = Square(2) #creates a Square of side 2

        #test if the area of the above square is 4 units
        #display an error message if its not
        self.assertEqual(sq.area(),4, f'Area is shown {sq.area()} for side = {sq.side} units')

    def test_area_negative(self):
        sq = Square(-3)
        self.assertEqual(sq.area(),-1,f'Area is shown {sq.area()} rather than -1')

    def test_perimeter(self):
        sq = Square(5)
        self.assertEqual(sq.perimeter(), 20, f'Perimeter is {sq.perimeter()} rather than 20')
    
    def test_perimeter_negative(self):
        sq = Square(-6)
        self.assertEqual(sq.perimeter(), -1, f'Perimeter is {sq.perimeter()} rather than -1')

if __name__ == '__main__':
    unittest.main()