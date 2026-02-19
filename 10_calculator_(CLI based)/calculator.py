#CALCULATOR CLI VERSION
import math
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def power(a,b):
    return math.pow(a, b)
def show_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")
def record_and_print_history(history, operation, num1, num2, result, sign=None):
    if sign:
        entry = f"{operation}: {num1} {sign} {num2} = {result}"
    else:
        entry = f"{operation}: {num1} and {num2} = {result}"
    history.append(entry)
    print(f"Result: {result}")

print("---------------------------------")
print("| Welcome to the Calculator CLI! |")
print("---------------------------------")
history = []
while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Show History")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ").strip()
    if choice == '6':
        show_history(history)
        continue
    if choice == '7':
        print("Goodbye!")
        break
    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            record_and_print_history(history, "Addition", num1, num2, result, sign="+")
        elif choice == '2':
            result = subtract(num1, num2)
            record_and_print_history(history, "Subtraction", num1, num2, result, sign="-")
        elif choice == '3':
            result = multiply(num1, num2)
            record_and_print_history(history, "Multiplication", num1, num2, result, sign="x")
        elif choice == '4':
            if num2==0:    
                print("Error: Division by zero is not allowed.")
            else:
                result = divide(num1, num2)
                record_and_print_history(history, "Division", num1, num2, result, sign="/")
        elif choice == '5':
                result = power(num1, num2)
                record_and_print_history(history, "Power", num1, num2, result, sign="^")
        else:
            print("Invalid choice. Please select a valid operation.")
