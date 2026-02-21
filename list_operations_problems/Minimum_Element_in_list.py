 #Find Minimum Element
 a=[8,3,15,2,10]

min_val = a[0]

for i in range(len(a)):
    if a[i] < min_val:
        min_val = a[i]

print(min_val)
