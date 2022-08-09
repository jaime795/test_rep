import sys, os, inspect

#get acces to the current directory and the parent directory in order to import modules from it
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)

from my_class import Square

#All tests must start with "test"
def test_file1_area():
    sq = Square(2)
    assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()} instead of 4"

def test_file1_perimeter():
    sq = Square(-1)
    assert sq.perimeter() == -1, f"perimeter is shown {sq.perimeter()} rather than -1"