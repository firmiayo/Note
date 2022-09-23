from math import sqrt
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
j=b**2-4*a*c
if j==0:
    print("X1 = X2 ={:.2f}".format((-b+sqrt(j))/2/a))
elif j>0:
    x1=(-b+sqrt(j))/2/a
    x2=(-b-sqrt(j))/2/a
    print("X1 = {:.2f} , X2 = {:.2f} ".format(x1,x2))
else:
    print("复合数")