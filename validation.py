from datetime import datetime


def get_integer(prompt, minimum=None, maximum=None):
    # Safely request an integer from the user.
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"ERROR: VALUE MUST BE AT LEAST {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"ERROR: VALUE MUST NOT EXCEED {maximum}.")
                continue

            return value

        except ValueError:
            print("ERROR: PLEASE ENTER A VALID INTEGER.")


def get_yes_no(prompt):
    # Request a Y/N response.
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return "y"
        if value in ("n", "no"):
            return "n"

        print("ERROR: PLEASE ENTER Y OR N.")


def get_date(prompt, date_format="%d-%m-%Y"):
    # Request and validate a date.
    while True:
        value = input(prompt).strip()

        try:
            datetime.strptime(value, date_format)
            return value

        except ValueError:
            print(f"ERROR: INVALID DATE. USE {date_format} FORMAT.")


def get_non_empty_string(prompt):
    # Request a string that cannot be empty.

    while True:
        value = input(prompt).strip()
        if value:
            return value

        print("ERROR: THIS FIELD CANNOT BE EMPTY.")


def get_choice(prompt, valid_choices):
    # Request a menu choice from a predefined set.

    while True:
        value = input(prompt).strip()
        if value in valid_choices:
            return value

        print(f"ERROR: INVALID INPUT. VALID OPTIONS: {', '.join(valid_choices)}")


def get_designation():
    # Request a valid Outset designation.
    valid_designations = {"1": "Manager", "2": "IGL", "3": "Gamer"}

    while True:
        print()
        print("SELECT DESIGNATION")
        print("1. Manager")
        print("2. IGL")
        print("3. Gamer")

        choice = get_choice("ENTER DESIGNATION - ", valid_designations.keys())

        return valid_designations[choice]


def get_game_name():
    # Request a valid game name.
    games = {"1": "Valorant", "2": "CS:GO", "3": "BGMI"}

    while True:
        print()
        print("SELECT GAME")
        print("1. Valorant")
        print("2. CS:GO")
        print("3. BGMI")

        choice = get_choice("ENTER GAME - ", games.keys())

        return games[choice]


def get_user_id():
    # Request a valid six-digit user ID.
    while True:
        value = input("ENTER USER ID OF MEMBER - ").strip()
        if value.isdigit() and len(value) == 6:
            return int(value)
        print("ERROR: USER ID MUST CONTAIN EXACTLY 6 DIGITS.")
