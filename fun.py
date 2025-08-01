def fibo(n):
    a,b=0,1
    print(a)
    print(b)
    i=2
    while i!=n:
        c=a+b
        print(c)
        a=b
        b=c
        i += 1
a= int(input("enter num : "))
fibo(a)
    
