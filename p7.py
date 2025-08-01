a = list()
b = ["honda" , "toyota" , "mahindra" ]
a.append("Apple")
a.append("Banana")
a.append("Water-melon")
c= [101 , 102 , 103 , 104 , 105 , 106]
print(a)

a.extend(b)
print(a)
print(b)

b.insert(2, "suzuki")
print(b)

print("length of string: " , len(a))
print("value of at 2 : " , a[2] )
a.reverse()
print(a)

if "Water-melon" in a:
    print("available")
else:
    print("not in the list")

print(c)
c.pop()
print(c)
c.remove(104)
print(c)
c.clear()
print(c)
