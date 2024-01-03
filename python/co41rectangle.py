class Rectangle:
   def __init__(self, length, bredth):
    self.length = length
    self.bredth = bredth
   def area(self):
     return self.length*self.bredth
   def perimeter(self):
     return 2*(self.length+self.bredth)
   
   
print("Rectangle 1\n")
length=int(input("enter the length:"))
bredth=int(input("enter the bredth:"))
rectangle1=Rectangle(length,bredth)
print("area of rectangle1",rectangle1.area())
print("perimeter of rectangle",rectangle1.perimeter())

print("\nRectangle 2\n")
length2=int(input("enter the length:"))
bredth2=int(input("enter the bredth:"))
rectangle2=Rectangle(length2,bredth2)
print("area of rectangle2",rectangle2.area())
print("perimeter of rectangle2",rectangle2.perimeter())
if rectangle1.area()==rectangle2.area():
 print("Area of rectangle1 and rectangle2 are equal.")
else:
 print("Area of rectangle1 and rectangle2 are not equal.")
