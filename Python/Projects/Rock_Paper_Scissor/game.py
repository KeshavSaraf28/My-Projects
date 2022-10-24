import random


def main():
    while True:
        print("\nEnter 'r' for rock, 'p' for paper, or 's' for scissors, 'q' for quit.")
        player = input("Enter your choice: ")
        if player == 'q':
            return
        computer = random.choice(['r', 'p', 's'])
        print("\nComputer choice : ", computer)
        if player == computer:
            print("It's a tie!")
        elif player == 'r' and computer == 's':
            print("You win!")
        elif player == 'r' and computer == 'p':
            print("You lose!")
        elif player == 'p' and computer == 'r':
            print("You win!")
        elif player == 'p' and computer == 's':
            print("You lose!")
        elif player == 's' and computer == 'r':
            print("You lose!")
        elif player == 's' and computer == 'p':
            print("You win!")
        else:
            print("Invalid input.")
        
        


if __name__ == '__main__':
    main()
