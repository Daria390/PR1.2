from math_calc import calculate_expression
from table_powers import display_powers_table

def main():
    while True:
        print("\nMain menu:")
        print("1. Calculate expression y = (sin(x) + x^2) / sqrt(x + 3)")
        print("2. Display squares and cubes table for (1, 3, 5, 9, 17)")
        print("0. Exit")
        
        choice = input("Choose option: ")

        
        if choice == "1":
            try:
                x = float(input("Enter value for x: "))
                result = calculate_expression(x)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: y = {result:.6f}")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == "2":
            display_powers_table()
            
        elif choice == "0":
            print("Program terminated.")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()