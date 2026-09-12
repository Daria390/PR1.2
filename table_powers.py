def display_powers_table():
    numbers = [1, 3, 5, 9, 17]
    
    print("\n" + "=" * 32)
    print(f"{'Number':^8}|{'Square':^10}|{'Cube':^12}")
    print("-" * 32)
    
    for num in numbers:
        square = num ** 2
        cube = num ** 3
        print(f"{num:^8}|{square:^10}|{cube:^12}")
        
    print("=" * 32 + "\n")