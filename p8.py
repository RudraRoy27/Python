

j = (1 , 2 , 3 , 4 , 5 , 6 , 7)
print(len(j))
sum=0
minv=1000
maxv=0
for i in j:
    sum = sum + i
    if i > maxv:
        maxv = i
    if i < minv:
        minv = i
print( "sum is : " , sum)
print( "min is : " , minv)
max_value = max(j)
min_value = min(j)
print("through function : max " , max_value)
print("through function : min " , min_value)
print( "max is : " , maxv)
