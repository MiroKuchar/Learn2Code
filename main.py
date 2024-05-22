from game import select_fighter, battle

def main():
    player1 = select_fighter(1)
    player2 = select_fighter(2)
    battle(player1, player2)

if __name__ == "__main__":
    main()
