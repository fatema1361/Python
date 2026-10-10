print("Simple Python Calculator!")
num1=float(input("Enter First number: "))
num2=float(input("Enter Second number: "))
operator=input("Enter Operator(+,-,*,/): ")
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    result=num1/num2
else:
    result="Operator Invalid!"


print("Result = ",result)