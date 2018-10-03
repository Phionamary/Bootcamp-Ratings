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
        return

    if len(password) < 5:
        print(
            "Password is too short. mut have atleats 5 characters")
        return
    print("\nYou have successfully signed up\n")
    print("\nYou can now login\n")
    username = input("Enter your user name: ")
    password = input("Enter your password: ")
    account_type = input("Enter account type: ")
    login(username, password, account_type)


def login(username, password, account_type):
    if len(password) < 5:
        print(
            "Password is too short. mut have atleats 5 characters")
        return
    print("\nYou have successfully loged in\n")
    after_login_options(account_type)


def after_login_options(account_type):
    if account_type == "LFA":
        print("To view scores press 1")
        print("To add scores press 2")
        scores_option = input()

        if scores_option == "1":
            print("Scores include Excellence, Passion, Integrity and collaboration")
            print("Scores list")
            print("\nBoot camper name: Paul")
            print(
                "Boot camper Scores: Excellence ( 2 ) , Passion ( 1 ), Integrity( 2 ),  collaboration ( 1 )")
            print("\nBoot camper name: Ahmad")
            print(
                "Boot camper Scores: Excellence ( 2 ) , Passion ( 2 ), Integrity( 1 ),  collaboration ( 2 )")
            exit = input("Press any key to exit")

        if scores_option == "2":
            print("Scores include Excellence, Passion, Integrity and collaboration")
            print("The scores range from -2 to 2")
            excellence = input("Add score for Excellence ")
            if not check_score(excellence):
                print("Invalid score")
                print("/n Repeat")
                after_login_options(account_type)
                return

            passion = input("Add score for Passion ")
            if not check_score(passion):
                print("Invalid score ")
                print("/n Repeat")
                after_login_options(account_type)
                return

            integrity = input("Add score for Integrity")
            if not check_score(integrity):
                print("Invalid score")
                print("/n Repeat")
                after_login_options(account_type)
                return

            collaboration = input("Add score for Collaboration")
            if not check_score(collaboration):
                print("Invalid score")
                print("/n Repeat")
                after_login_options(account_type)
                return

    if account_type == "LF":
        print("To view scores press 1")
        scores_option = input()
        if scores_option == "1":
            print("Scores include Excellence, Passion, Integrity and collaboration")
            print("Scores list")
            print("\nBoot camper name: Paul")
            print(
                "Boot camper Scores: Excellence ( 2 ) , Passion ( 1 ), Integrity( 2 ),  collaboration ( 1 )")
            print("\nBoot camper name: Ahmad")
            print(
                "Boot camper Scores: Excellence ( 2 ) , Passion ( 2 ), Integrity( 1 ),  collaboration ( 2 )")
            exit = input("Press any key to exit")


def check_score(score):
    """Vlalidates score"""

    if int(score) >= -2 and int(score) <= 2:
        return True
    else:
        return False


def add_scores(e, p, i, c):
    pass


if option == "l":
    print("\nYou are ready to Login: ")
    username = input("Enter your user name: ")
    password = input("Enter your password: ")
    account_type = input("Enter account type: ")
    login(username, password, account_type)

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
