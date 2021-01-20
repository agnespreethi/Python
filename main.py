ch = '*'
a=input()
for i in range(1,(10)):
    if(i==5 or i==6 or i==7):
        print(ch,end="")
    else:
        print(end=" ")
print()
for i in range(1,(10)):
    if(i==4 or i==8):
        print(ch,end="")
    else:
        print(end=" ")
        
print()
for i in range(1,(10)):
    if(i==4 or i==8):
        print(ch,end="")
    else:
        print(end=" ")
        
print()
for i in range(1,(10)):
    if(i==4 or i==5 or i==6 or i==7 or i==8):
        print(ch,end="")
    else:
        print(end=" ")
        
print()
for i in range(1,(10)):
    if(i==4 or i==8):
        print(ch,end="")
    else:
        print(end=" ")
        
print()
for i in range(1,(10)):
    if(i==4 or i==8):
        print(ch,end="")
    else:
        print(end=" ")

print()
for i in range(1,(10)):
    if(i==4 or i==8):
        print(ch,end="")
    else:
        print(end=" ")
print()
x = input()
for i in range(6):
    for j in range(7):
        if (i==0 and j %3 !=0) or (i==1 and j %3 ==0) or (i-j==2) or (i+j==8):
            print("\U0001F60D",end=" ")
        else:
            print(" ",end=" ")
    
    print()        
