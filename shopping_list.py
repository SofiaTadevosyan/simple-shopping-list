shopping_list = []

def show_items():
    """Display the current shopping list."""
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("\nYour shopping list is empty.")
    print()

def add_item():
    """Add an item to the shopping list."""
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.\n")

def main():
    """Main function to run the Shopping List App."""
    while True:
        print("Shopping List App")
        print("1. View Shopping List")
        print("2. Add Item")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            show_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            print("Exiting the Shopping List app. Goodbye!")
            break
        else:
            print("Invalid option, please choose again.\n")

if __name__ == "__main__":
    main()
