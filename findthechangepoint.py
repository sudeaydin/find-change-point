a=[0,1,1,1,1,1,1]
N=len(a)
found=0
middle=int((N-1)/2)
while  found==0:
    if a[middle]==1:
        if a[middle]!=a[middle-1]:
            found=1
            print("Zeros ends in {0} and ones starts in {1} ".format(middle,middle+1))
        else:
            middle=middle-1
    elif a[middle]!=a[middle+1]:
        found=1
        print("Zeros ends in {0} and ones starts in {1} ".format(middle+1,middle+2))
    else:
        middle=middle+1
