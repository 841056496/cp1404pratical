"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "C:\cp1404pratical\prac_04\subject_data"

def get_data():
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer
            data.append(parts)
    return data

def display_subject_details(data):
    for subject in data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

def main():
    data = get_data()
    display_subject_details(data)

main()
