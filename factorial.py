def fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    print("factorial = : " , fa)

a= int(input("enter num : " ))
fact(a)
