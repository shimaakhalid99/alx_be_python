def perform_operation(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        if num2 == 0:
            return f"can't recognize this value."
        else:
            return num1/num2
