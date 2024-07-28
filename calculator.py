print("\nWhich operation you want to perform?(for arthematic and comparision type AC and for logical type L)")
Choose=input("Type your choice:(AC/L): ")
if Choose=="AC":
    print("\nwell, you choose Arithematic and comparision operation")
    a=int(input("Enter the first number: "))

    operator=input("Enter the operator:(Arithmatic operator and comparision operator is valid)")

    b=int(input("Enter the second number: "))

    #Arithmatic operator
    if operator=='+':
        print(a+b)
    elif operator=='-':
        print(a-b)
    elif operator=='*':
        print(a*b)
    elif operator=='/':
        print(a/b)
    elif operator=='%':
        print(a%b)

    #Comparision
    elif operator=="<":
        c=a<b
        print(c)
    elif operator=="==":
        c=a==b
        print(c)
    elif operator==">":
        c=a>b
        print(c)
    elif operator=="<=":
        c=a<=b
        print(c)
    elif operator==">=":
        c=a>=b
        print(c)
    elif operator=="!=":
        c=a!=b
        print(c)
    else:
        print("Operation is invalid")

#for logical operation
else:
    x=input("Enter the first logic: ")
    op=input("Enter the operator: ")
    y=input("Enter the second logic: ")
    if op=="and":
        z=x and y
        print(z)
    elif op=="or":
        z=x or y
        print(z)
    elif op=="not":
        take=input("For x type 'x' or for y type 'y'")
        if take=="x":
            z=not(x)
            print(z)
        elif take=="y":
            z=not(y)
            print(z)
