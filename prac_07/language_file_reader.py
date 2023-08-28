import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()  # Consume the first line
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)

# Other functions like using_csv, using_namedtuple, etc. should be updated similarly to process the new column.

if __name__ == "__main__":
    main()
