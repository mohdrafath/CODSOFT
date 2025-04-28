#Task 2 - Calculator
def calculator():
    print("Simple Calculator\n")
    
    while True:
        # Get first number with validation
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Get operation with validation
        while True:
            op = input("Choose operation (+, -, *, /): ")
            if op in ['+', '-', '*', '/']:
                break
            print("Invalid operation! Please choose +, -, *, or /")

        # Get second number with validation
        while True:
            try:
                num2 = float(input("Enter second number: "))
                if op == '/' and num2 == 0:
                    print("Cannot divide by zero! Try another number.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Perform calculation
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2

        # Display result
        print(f"\n{num1} {op} {num2} = {result:.2f}\n")

        # Ask to continue
        cont = input("Another calculation? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye!")
            break
        print()

if __name__ == "__main__":
    calculator()
