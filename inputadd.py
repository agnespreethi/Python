x = int(input("enter the value1:"))
y = int(input("enter the value2:"))
z = x + y
print(z)


def add(a,b):
   return a+b

def sub(a,b):
   return a-b

def mul(a,b):
   return a*b

def div(a,b):
   return a//b

print("""choices:
1.add
2.sub
3.mul
4.div""")

choice=int(input("enter a choice:"))
a=int(input("enter value1:"))
b=int(input("enter value2:"))

if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print("no more choices")


    
    
