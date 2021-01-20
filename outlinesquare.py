n=6
i=0
while i<n:
    j=0
    while j<n:
        if(i==0 or i==n-1 or (j==0 or j==5) or j==j-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
