from graphics import square,triangle
#using square
a=int(input("enter the side: "))
print("area of a square =",square.area(a))
print("perimeter of a square=",square.perimeter(a))
#using triangle
b=int(input("enter the length :"))
h=int(input("enter the height :"))
print("area of right angled triangle =",triangle.area(b,h))
