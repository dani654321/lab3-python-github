import numpy as np

def calculate_addition(addend1, addend2):
    return np.add(addend1, addend2)

def calculate_subtraction(minuend, subtrahend):
    return np.subtract(minuend, subtrahend)

def calculate_multiplication(multiplier, multiplicand):
    return np.multiply(multiplier, multiplicand)

def calculate_division(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return np.divide(dividend, divisor)

def calculate_percentage(smaller_number, bigger_number):
    if bigger_number == 0:
        return "Error: Cannot calculate percentage with a denominator of zero."
    return np.divide(smaller_number, bigger_number) * 100

def even_odd_check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main calculator loop
while True:
    # 1. Get inputs safely
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue  # Restarts the loop to ask for numbers again

    operation = input("Enter the operation (+, -, *, /, %): ")
    result = None

    # 2. Process operations
    if operation == '+':
        result = calculate_addition(a, b)
    elif operation == '-':
        result = calculate_subtraction(a, b)
    elif operation == '*':
        result = calculate_multiplication(a, b)
    elif operation == '/':
        result = calculate_division(a, b)
    elif operation == '%':
        result = calculate_percentage(a, b)
    else:
        print("Invalid operation selection.")
        continue

    # 3. Print results
    print("Result:", result)
        # --- NEW: Separate Even/Odd Check Block ---
    # Only offer this check if the result is a valid number
    if isinstance(result, (int, float)):
        while True:
            check_even_odd = input("Do you want to check if this result is even or odd? (y/n): ").strip().lower()
            if check_even_odd == 'y':
                # Convert to integer if it's a whole float (e.g., 4.0 -> 4) to avoid modulo issues
                if result % 1 == 0:
                    status = even_odd_check(int(result))
                    print(f"The result ({int(result)}) is: {status}")
                else:
                    print(f"The result ({result}) is a decimal number, so it cannot be strictly even or odd.")
                break
            elif check_even_odd == 'n':
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

    # 4. Valid/Invalid choice handling to continue calculation
    while True:
        choice = input("\nEnter the choice if you want to continue or not (y/n): ").strip().lower()
        if choice == 'y':
            break  
        elif choice == 'n':
            print("Goodbye!")
            exit()  
        else:
            print("Invalid choice. Going back to choice selection.")
