MIN_LENGTH = 6


def main():

    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Password length must be 6 or more characters.")
        password = input("Please enter your password: ")

    stars = len(password) * '*'
    print(stars)


main()
