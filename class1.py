# Create a simple calculator using basic python

def calculate(a,b,op):
    if op in ["+","-","/","*"]:
        t=eval(str(a) + op +str(b))
        print(t)
a=int(input("a:"))
b=int(input("b:"))
op=input("Operatior:")

calculate(a,b,op)
print("=====================================================")
    
# Area of circle

def Area(r):
    print("Area of circle:",3.14*(r**2))

r = int(input("Radius:"))
Area(r)

print("=====================================================")

#Eligible for vote or not

def Vote(n):
    if n>18:
        print("Elligible for Vote")
    elif 0<n<=18:
        print("Not Elligible for Vote")
        print("Eligible in next",18-n,"year")

n=int(input("Age:"))
Vote(n)
print("=====================================================")













