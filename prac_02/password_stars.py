"""Password Check Program"""

def main():
    password = get_password()
    print_password_stars(password)

def get_password():
    MIN_PASSWORD_LENGTH = 8

    while True:
        password = input("Enter a password: ")
        if len(password) < MIN_PASSWORD_LENGTH:
            print("Password is too short. Minimum length is", MIN_PASSWORD_LENGTH)
        else:
            return password

def print_password_stars(password):
    print("*" * len(password))

# Call the main function to start the program
main()
