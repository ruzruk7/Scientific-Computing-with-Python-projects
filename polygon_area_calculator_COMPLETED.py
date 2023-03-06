class Rectangle:
    '''initialize a Rectangle class'''
    def __init__(self, width, height): 
        '''initialize properties available to rectangle'''
        self.width = width
        self.height = height

    def __str__(self):
        '''return the class instance call as a readable string'''
        return (f'Rectangle(width={self.width}, height={self.height})')
    def set_width(self, width):
        '''change the width attribute'''
        self.width = width
        # width = self.width

    def set_height(self, height):
        '''change the height attribute'''
        self.height = height
        # height = self.height

    def get_area(self):
        '''give the area within the rectangle'''
        area = (int(self.width) * int(self.height))
        return (area)
    
    def get_perimeter(self):
        '''give the perimeter of the rectangle'''
        perimeter = (self.width * 2 + self.height * 2) 
        return (perimeter)     
    
    def get_diagonal(self):
        '''give the diagonal length of the rectangle'''
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return (diagonal)
    
    def get_picture(self):
        '''display the rectangle using \'*\''''
        if self.width > 50 or self.height > 50:
            return ('Too big for picture.')
        else:
            horiz = ['*' for x in range(self.width)]
            z = ((''.join(horiz)) + ('\n')) * (self.height)
            # vert = [ for x in range(self.height)]
            return (z)
        # for wid in range(int(self.width)):

    def get_amount_inside(self, shape):
        return (self.get_area() // shape.get_area())

            

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
    def __str__(self):
        return(f'Square(side={self.width})')
    
    def set_side(self, set_side):
        self.width = set_side
        self.height = set_side
        
         
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
