import os;
file = input("file name first : ");
name,ext = os.path.split(file);
print(ext)
print(name)
