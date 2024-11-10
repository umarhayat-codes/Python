# Make three sides of a triangle as input and check if they form a valid triangle.
a = int(input('Enter first side of a triangle: '))
b = int(input('Enter second side of a triangle: '))
c = int(input('Enter third side of a triangle: '))

if (a + b == c) or (a + c == b) or (b + c == a):
    print("Triangle! ")
else:
    print("Not Trianlge! ")
