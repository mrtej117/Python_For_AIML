angle1 = int(input("enter the first angle : "))
angle2 = int(input("enter the second angle: "))

angle3 = 180-(angle1 + angle2)

print("third angle is ",angle3)
 
if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print(" invalid triangle containing negative values ")

else:
    print("third angle is ",angle3)

if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("right angled triangle")
elif angle1 ==angle2 or angle2== angle3 or angle1 ==angle3:
    print("Isosceles triangle")
else:
    print("neither")
