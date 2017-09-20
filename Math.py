#Analyzes 2 inputs and shows all the computations you can do with it
#Could be expanded to include area and circumferences, distance between eachother on a graph, etc.
#Problems so far: the 2nd part of the division function doesn't display the full decimal. 

x = input('What is the first number?: ')
y = input('What is the second number?: ')
pi = 3.14159265359

def addition():
    print('If you added '+str(x)+' and '+str(y)+', you would get...')
    print(x+y)
    print('')

def subtraction():
    print('If you subtracted '+str(y)+' from '+str(x)+', you would get...')
    print(x-y)
    print('')
    print('If you subtracted '+str(x)+' from '+str(y)+', you would get...')
    print(y-x)
    print('')

def multiplication():
    print('If you multiplied '+str(x)+' and '+str(y)+', you would get...')
    print(x*y)
    print('')

def division():
    print('If you divided '+str(x)+' by '+str(y)+', you would get...')
    print(float(x/y))
    print('')
    print('If you divided '+str(y)+' by '+str(x)+', you would get...')
    print(float(y/x))
    print('')

def exponents():
    print('If you squared '+str(x)+', you would get...')
    print(x**2)
    print('')
    print('If you squared '+str(y)+', you would get...')
    print(y**2)
    print('')
    print('If '+str(x)+' was the base, and '+str(y)+' was the exponent, you would get...')
    print(x**y)
    print('')
    print('If '+str(y)+' was the base, and '+str(x)+' was the exponent, you would get...')
    print(y**x)
    print('')

def area():
    print('If '+str(x)+' and '+str(y)+' were the length and width of a rectangle, the perimeter of that rectangle would be...')
    print((x+y)*2)
    print('')
    print('If '+str(x)+' and '+str(y)+' were the base and hight of a triangle, the area of that triangle would be...')
    print((x*y)/2)
    print('')
    print('If '+str(x)+' was the radius of a circle, that circle would have an area of...')
    print(pi*(x**2))
    print('')
    print('If '+str(y)+' was the radius of a circle, that circle would have an area of...')
    print(pi*(y**2))
    print('')
    print('If '+str(x)+' was the radius of a circle, that circle would have an circumference of...')
    print(2*pi*x)
    print('')
    print('If '+str(y)+' was the radius of a circle, that circle would have an circumference of...')
    print(2*pi*y)
    print('')

print('')
addition()
subtraction()
multiplication()
division()
exponents()
area()
print('Interesting.')