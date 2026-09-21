number1=int(input("Enter 1st no= "))
number2=int(input("Enter 2nd no= "))
operator=int("Enter operation - + * / % : ")

if(operator=="-"):
    print(number1-number2)
if(operator=="+"):
    print(number1+number2)
elif(operator=="*"):
    print(number1*number2)
elif(operator=="/"):
    print(number1/number2)
elif(operator=="%"):
    print(number1%number2)
else:
    print("invalid operator")
