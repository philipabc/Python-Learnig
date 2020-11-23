number=float(input("Please enter the first number: "))
number2=float(input("Please enter the second number: "))
op=(input("now please enter your operator: "))
if op=="+":
    print(number+number2)
elif op=="-":
        print(number-number2)
elif op=="*":
            print(number*number2)
elif op=="/":
    print(number/number2)            
elif op=="**":
    print(number**number2)
else:
    print("invalid operator")