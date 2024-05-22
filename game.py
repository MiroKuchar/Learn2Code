import time
from fighter import Fighter

def select_fighter(player_num):
    print(f"Player {player_num}, choose your fighter:")
    print("1. Warrior (100 HP, 20 DMG, 1 second hit timer, 0.7 hit rating, 0.2 dodge rating, 50% critical chance)")
    print("2. Archer (80 HP, 25 DMG, 1.5 second hit timer, 0.8 hit rating, 0.4 dodge rating, 30% critical chance)")
    print("3. Mage (60 HP, 30 DMG, 2 second hit timer, 0.9 hit rating, 0.1 dodge rating, 40% critical chance)")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        fighter = Fighter("Warrior", 100, 20, 1, 0.7, 0.2, 5)
    elif choice == '2':
        fighter = Fighter("Archer", 80, 25, 1.5, 0.8, 0.4, 3)
    elif choice == '3':
        fighter = Fighter("Mage", 60, 30, 2, 0.9, 0.1, 4)
    else:
        print("Invalid choice. Please try again.")
        return select_fighter(player_num)
    print()
    return fighter

def battle(player1, player2):
    print(f"Player 1: {player1.name}")
    print(f"Player 2: {player2.name}")

    print("Let the battle begin!")

    while player1.is_alive() and player2.is_alive():
        player1_dmg, player1_critical = player1.attack(player2)
        player2_dmg, player2_critical = player2.attack(player1)

        if player1_dmg > 0:
            player2.hp -= player1_dmg
            player2.hp = max(player2.hp, 0)
            if player1_critical:
                print(f"{player1.name} hits {player2.name} for {player1_dmg} damage! (Critical Hit)")
            else:
                print(f"{player1.name} hits {player2.name} for {player1_dmg} damage!")
        else:
            print(f"{player1.name} missed the attack!")

        if not player2.is_alive():
            break

        if player2_dmg > 0:
            player1.hp -= player2_dmg
            player1.hp = max(player1.hp, 0)
            if player2_critical:
                print(f"{player2.name} hits {player1.name} for {player2_dmg} damage! (Critical Hit)")
            else:
                print(f"{player2.name} hits {player1.name} for {player2_dmg} damage!")
        else:
            print(f"{player2.name} missed the attack!")

        print(f"{player1.name} HP: {player1.hp}")
        print(f"{player2.name} HP: {player2.hp}")
        print()

        time.sleep(0.5)  # Adjust sleep time to half a second

    if player1.is_alive() and not player2.is_alive():
        print(f"{player1.name} wins!")
    elif player2.is_alive() and not player1.is_alive():
        print(f"{player2.name} wins!")
    else:
        print("It's a draw!")
