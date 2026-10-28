def run_cafe_billing():
    # 1. Define the menu using a dictionary
    menu = {
        "Espresso": 2.50,
        "Latte": 3.50,
        "Cappuccino": 3.75,
        "Croissant": 3.00,
        "Muffin": 2.75,
        "Cheesecake": 4.50
    }
    
    order = {}
    print("=" * 35)
    print("    WELCOME TO THE PYTHON CAFE    ")
    print("=" * 35)
    
    # 2. Display the menu
    for item, price in menu.items():
        print(f" {item:<15} : ${price:.2f}")
    print("=" * 35)
    
    # 3. Order taking loop
    while True:
        choice = input("\nEnter the item name to order (or type 'bill' to finish): ").strip()
        
        if choice.lower() == 'bill':
            break
            
        # Match case-insensitively with the menu keys
        matched_item = next((k for k in menu if k.lower() == choice.lower()), None)
        
        if matched_item:
            try:
                quantity = int(input(f"How many {matched_item}s would you like? "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                order[matched_item] = order.get(matched_item, 0) + quantity
                print(f"Added {quantity}x {matched_item} to your cart.")
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")
        else:
            print("Item not found on the menu. Please check the spelling.")
            
    if not order:
        print("\nNo items ordered. Have a nice day!")
        return

    # 4. Calculate Subtotal, Tax, and Grand Total
    subtotal = sum(menu[item] * qty for item, qty in order.items())
    tax = subtotal * 0.05  # 5% Tax rate
    total = subtotal + tax
    
    # 5. Print final formatted receipt
    print("\n" + "=" * 40)
    print("             FINAL RECEIPT            ")
    print("=" * 40)
    print(f"{'Item':<18}{'Qty':<6}{'Price':<8}{'Total':<8}")
    print("-" * 40)
    
    for item, qty in order.items():
        item_total = menu[item] * qty
        print(f"{item:<18}{qty:<6}${menu[item]:.2f}   ${item_total:.2f}")
        
    print("-" * 40)
    print(f"{'Subtotal:':<32}${subtotal:.2f}")
    print(f"{'Tax (5%):':<32}${tax:.2f}")
    print("-" * 40)
    print(f"{'Grand Total:':<32}${total:.2f}")
    print("=" * 40)
    print("       Thank you for visiting!        \n")

if __name__ == "__main__":
    run_cafe_billing()
