# match_case_calculator.py

# استدعاء أرقام المستخدم
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# اختيار العملية
operation = input("Choose the operation (+, -, *, /): ")

# تنفيذ العملية باستخدام Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
