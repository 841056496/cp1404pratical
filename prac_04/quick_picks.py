import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)

def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()
    return quick_pick

def print_quick_pick(quick_pick):
    for num in quick_pick:
        print(f"{num:2}", end=" ")
    print()

if __name__ == "__main__":
    main()
