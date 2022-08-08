class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4
    
    def __repr__(self):
        #Declares how a Square object should be printed
        #str() computes the informal string representation of an object
        #repr() compute the official string representation of an object, use for debugging
        s = 'Sqaure with side = ' + str(self.side) + '\n' + "Area = " + str(self.area()) + "\n" + "Perimeter = " + str(self.perimeter())
        return s

if __name__ == '__main__':
    #Read from user
    side = eval(input('Enter the side length to create a Square: '))

    #Create a square with that side
    square = Square(side)

    #print the created square
    print(square)
        