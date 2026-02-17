lenght= int(input("enter value lenght : "))
widht = int(input("enter value breadth : "))
area =  lenght * widht
perimeter = 2 * (length+breadth)
print(area)
#######################33333333333333333333333333333333333333333333333333
def area_perimeter(length,breadth):
    area = length * breadth
    perimeter = 2 * (length+breadth)
    return area,perimeter
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
c =area_perimeter(l,b)
print(c)
