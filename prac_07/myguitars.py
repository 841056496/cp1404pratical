from guitar import Guitar

def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars_to_file(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    guitars = read_guitars_from_file("guitars.csv")
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()  # Sort guitars by year

    # Add user's new guitars
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    save_guitars_to_file("guitars.csv", guitars)
    print("Guitars saved.")

if __name__ == "__main__":
    main()
