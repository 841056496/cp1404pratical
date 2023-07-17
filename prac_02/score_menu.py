import random

def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    else:
        return "Excellent"

def print_result(score):
    print(determine_score_status(score))

def show_stars(score):
    print('*' * int(score))

def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def main():
    print("Welcome!")
    score = get_valid_score()
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
