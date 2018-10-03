from re import match

print("\nWelcome to Bootcamp rating app.\n")
print("To sign up Press: s")
print("To login press: l")

option = input()


def signup(username, email, password, account_type):
    if not bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                email)):
        print("Email is not valid. use example email soko@andela.com")

    if len(password) < 5:
        print(
            "Password is too short. mut have atleats 5 characters")


if option == "l":
    print("\nYou are ready to Login: ")
    username = input("Enter your user name: ")
    password = input("Enter your password: ")

if option == "s":
    print("\nYou are ready to Signup: \n")
    print("\nYou can sign up as LF, LFA or Boot camper\n")
    print("To sign up as LF press: 1")
    print("To sign up as LFA press: 2")
    print("To sign up as Boot camper press: 3")
    signup_option = input()
    if signup_option == "1":
        print("\nYou are signing up as LF\n")
        username = input("Enter your user name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        signup(username, email, password, "LF")

    if signup_option == "2":
        print("\nYou are signing up as LFA\n")
        username = input("Enter your user name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        signup(username, email, password, "LFA")

    if signup_option == "3":
        print("\nYou are signing up as Boot camper\n")
        username = input("Enter your user name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        signup(username, email, password, "Boot camper")
