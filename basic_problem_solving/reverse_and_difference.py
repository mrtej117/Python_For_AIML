  num = int(input("Enter a 4-digit number: "))

original = num     

d1 = num % 10
num = num // 10
d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10    # it will be obtained by using the reminder formula 

reversed_num = d1*1000 + d2*100 + d3*10 + d4

difference = original - reversed_num

print("Reversed:", reversed_num)
print("Difference:", difference)


# a=4%  10
# print(a)
