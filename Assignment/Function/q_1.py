def area_of_circle(radius):
    pi = 3.14
    area = 2 * pi * radius
    return area

radius = int(input("Enter radius to calculate area: "))
print(area_of_circle(radius))