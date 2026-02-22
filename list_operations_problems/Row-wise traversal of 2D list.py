a = [[1,2,3,4,5,6,7,8],
      [9,10,11,12,13,14,16]]
print(a[0])
print(len(a))
print(len(a[0]))

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end = " ")
        print()
