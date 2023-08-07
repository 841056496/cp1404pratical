import csv
def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        return [row for row in reader][1:]

def process_champions(data):
    champions = {}
    countries = set()
    for row in data:
        champion_name = row[2]
        country = row[1]
        champions[champion_name] = champions.get(champion_name, 0) + 1
        countries.add(country)
    return champions, countries

def display_champions(champions):
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

def display_countries(countries):
    sorted_countries = sorted(list(countries))
    print("\nThese {} countries have won Wimbledon:".format(len(sorted_countries)))
    print(", ".join(sorted_countries))

def main():
    filename = "wimbledon.csv"
    data = read_file(filename)
    champions, countries = process_champions(data)
    display_champions(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()
