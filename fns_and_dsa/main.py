from arithmetic_operations import perform_operation
from shopping_list_manager import display_menu
from explore_datetime import display_current_datetime, calculate_future_date
from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

def main():

    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to add: ")
            item = item.strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == 2:
            item = input("Enter the item to remove: ")
            item = item.strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        elif choice == 3:
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

    print("\nCurrent Date and Time:")
    display_current_datetime()

    print("\nCalculate a Future Date:")
    calculate_future_date()

    print("\nTemperature Conversion Tool")
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
