def summa(x,z,y):
    if z=="-":
        Diferends=a-c
        return Diferends
    elif z=="+":
        Summa=a+c
        return Summa
    elif z=="*":
        Product=a*c
        return Product
    elif z=="/":
        if c>0 and a>0:
            Division=a/c
            return Division
        else:
            return "Error"
a=int(input("Enter first number: "))
b=input("Enter action: ")
c=int(input("Enter second number: "))
print(summa(a,b,c))

