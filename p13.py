import re
a=input("enter string : ")
if len(a)<3:
    print(a)
else:
    match = re.sub("ing", "ly", a)
    print(match)
        

