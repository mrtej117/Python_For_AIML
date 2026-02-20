def square(side):
    area = side * side
    perimeter = 4 * side
    return(area,perimeter)
side = int(input("Enter the side of square: "))    
a,p = square(side)
print("area",a)
print("perimenter",p)
