#  1
name = input("Please enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

#  2
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Your name is {name}")

#  3
with open("numbers.txt", "r") as file:
    line1 = int(file.readline())
    line2 = int(file.readline())
total = line1 + line2
print(f"The sum of the first two numbers is: {total}")

#  4
with open("numbers.txt", "r") as file:
    lines = file.readlines()
total = sum(int(line) for line in lines)
print(f"The sum of all numbers is: {total}")
