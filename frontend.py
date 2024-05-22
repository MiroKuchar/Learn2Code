from game import select_fighter, battle

def display_menu():
    print("\nWelcome to the Arena - Tvoj Tatko je buzerant!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            player1 = select_fighter(1)
            player2 = select_fighter(2)
            battle(player1, player2)
        elif choice == '2':
            print("Thank you for playing!")
            break
        else:
            print("Your Selection was Invalid. Please try again.")

if __name__ == "__main__":
    main()
