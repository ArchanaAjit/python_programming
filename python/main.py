from graphics import rectangle,circle
from graphics.ThreeDgraphics import cuboid,sphere 
#using rectangle module
length=int(input("enter the length: "))
width=int(input("enter the width: "))
print("area of a rectangle =",rectangle.area(length,width))
print("perimeter of a rectangle =",rectangle.perimeter(length,width))
#using circle module
r=int(input("enter the radius: "))
print("area of the circle =",circle.area(r))
print("perimeter of circle=",circle.perimeter(r))
#using cuboid module
l=int(input("enter the length: "))
w=int(input("enter the width: "))
h=int(input("enter the height: "))
print("area of cuboid=",cuboid.area(l,w,h))
print("volume of cuboid=",cuboid.volume(l,w,h))
#using sphere module
r=int(input("enter the radius: "))
print("area of sphere=",sphere.area(r))
print("volume of sphere=",sphere.volume(r))

