status='Y'
while status=='Y':
    n1=int(input("Enter a number:"))
    n2=int(input("Enter a number"))
    s1=n1
    s2=n2
    if n2>n1:
        s1=n2
        s2=n1
    for i in range(s2,s1+1):
        if s1%i==0:
            f=i
            break
    su=0
    while f!=0:
        ld=f%10
        su+=ld
        f//=10
    print("The number is",su)
    status=input("Do you want to continue(Y/N):")
    
    status=status.upper()
    if status=='N':
        print("Program Terminated")
