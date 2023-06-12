x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
op = input("Enter operator: (+, -, *, /)")
if op == '+':
    print("/nThe sum: ", x + y)
elif op == '-':
    print("/nThe difference: ", x - y)
elif op == '*':
    print("/nThe product: ", x * y)
elif op == '/':
    print("/nThe quotient: ", x / y)
else:
    print("/nInvalid operator!")