import math

#SOLVE store side argument from Square class in height and width in parent class
#SOLVE have set width and hight should set both width and hight 
class Rectangle :
    def __init__(self, width, height):
        self.height = int(height) 
        self.width = int(width)

    def __str__(self):
        print(f"Rectangle(width={self.width}, height={self.height})")
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width 

    def set_height(self, height):
        self.height = height

    def get_area(self):
        x = (self.height * self.width)
        return x
        
    def get_perimeter(self):
        x = (2 * self.width) + (2 * self.height)
        return x 
    
    def get_diagonal(self):
        x = math.sqrt(self.width ** 2 + self.height ** 2)
        print(x)
        return (x)

    def get_picture(self):
        print("x")
        if self.width and self.height < 50 :
            string = ""
            row = f"{self.width * '*'}\n"
            for i in range(self.height):
                string += row 
            return string 
        else : 
            print("Too big for picture.")
            return "Too big for picture."

    def get_amount_inside(self, shape):
        lateral_total = 0
        x = self.width
        while x >= shape.width :
            x -= shape.width
            lateral_total += 1
        vertical_total = 0
        y = self.height 
        while y >= shape.height :
            y -= shape.height
            vertical_total += 1

        total_fits = lateral_total * vertical_total
        print(lateral_total, vertical_total, total_fits)
        return total_fits

#would be cool to make the generation of these instances contingent on whether the sides were of equal length 
#creating a new init gets an error cuz its overriding the father class init and passing to many initial arguments
class Square(Rectangle):  
    
    def __init__(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
        if self.check() == False : 
            self.__del__()
            print("Finger wag")
        else :
            return print("you have a square")

    def __str__(self):
        print(f"Square(side={self.width})")
        return f"Square(side={self.width})"

    def _del_(self):
        print("object deleted")
    
    def check(self):
        if self.width != self.height:
            print("that aint a square")
            return False
    def set_side(self, side):
        self.width = side 
        self.height = side

    def set_height(self, height):
        super().set_width(height)
        return super().set_height(height)

    def set_width(self, width):
        super().set_height(width)
        return super().set_width(width)
            


a = Rectangle(50, 10)

a.get_diagonal()










