import os
from pathlib import Path

from dotenv import load_dotenv

from database import (
    get_connection,
    load_members,
    add_member
)

from authentication import authenticate_user

from game_data import (
    load_game_data,
    add_game_record,
    save_game_data
)

from validation import (
    get_integer,
    get_yes_no,
    get_date,
    get_non_empty_string,
    get_choice,
    get_designation,
    get_game_name,
    get_user_id
)

from visualization import view_data


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


DATA_DIR = Path(
    os.getenv(
        "GAME_DATA_DIR",
        BASE_DIR / "data"
    )
)


DB_CONFIG = {
    "host": os.getenv(
        "DB_HOST",
        "localhost"
    ),

    "user": os.getenv(
        "DB_USER",
        "root"
    ),

    "password": os.getenv(
        "DB_PASSWORD"
    ),

    "database": os.getenv(
        "DB_NAME",
        "outset"
    )
}


GAME_FILES = {
    "Valorant":
        DATA_DIR / "ValorantData.csv",

    "CS:GO":
        DATA_DIR / "CSGOData.csv",

    "BGMI":
        DATA_DIR / "BGMIData.csv"
}


# ============================================================
# GAME OPERATIONS
# ============================================================

def select_game_data():
    """
    Ask the user which game's data they want to access.
    """

    game_name = get_game_name()

    print(
        f"ACCESSING {game_name.upper()} DATABASE..."
    )

    dataframe = load_game_data(
        game_name,
        GAME_FILES
    )

    return game_name, dataframe


def edit_game_data(game_name, dataframe):
    """
    Add game records and persist them to CSV.
    """

    print()
    print(
        f"YOU CHOSE TO EDIT THE DATA OF {game_name}"
    )

    print()

    print(dataframe.to_string(index=False))

    while True:

        print()

        date = get_date(
            "ENTER DATE (DD-MM-YYYY) - "
        )

        games_won = get_integer(
            "ENTER GAMES WON - ",
            minimum=0
        )

        games_lost = get_integer(
            "ENTER GAMES LOST - ",
            minimum=0
        )

        rounds_won = get_integer(
            "ENTER ROUNDS WON - ",
            minimum=0
        )

        rounds_lost = get_integer(
            "ENTER ROUNDS LOST - ",
            minimum=0
        )

        # --------------------------------
        # ADD RECORD
        # --------------------------------

        dataframe = add_game_record(
            dataframe,
            date,
            games_won,
            games_lost,
            rounds_won,
            rounds_lost
        )

        # --------------------------------
        # SAVE IMMEDIATELY
        # --------------------------------

        save_game_data(
            dataframe,
            game_name,
            GAME_FILES
        )

        print()
        print("RECORD ADDED SUCCESSFULLY.")

        again = get_yes_no(
            "DO YOU WANT TO EDIT DATA AGAIN? (Y/N) "
        )

        if again == "n":
            break

    return dataframe


# ============================================================
# MANAGER FUNCTIONS
# ============================================================

def manager_game_menu():
    """
    Manager's game-data menu.
    """

    while True:

        print()
        print("PRESS 1 FOR EDITING THE DATA")
        print("PRESS 2 FOR VIEWING THE DATA")

        choice = get_choice(
            "--------> ",
            {"1", "2"}
        )

        game_name, dataframe = select_game_data()

        if choice == "1":

            dataframe = edit_game_data(
                game_name,
                dataframe
            )

        elif choice == "2":

            print(
                f"YOU CHOSE TO VIEW THE DATA OF "
                f"{game_name}"
            )

            view_data(dataframe)

        cont = get_yes_no(
            "DO YOU WANT TO CONTINUE? (Y/N) "
        )

        if cont == "n":
            break


def add_new_member(connection, members):
    """
    Add a new member to the database.
    """

    print()
    print("ADDING A MEMBER TO THE OUTSET DATABASE")
    print("ENTER MEMBER DETAILS...")
    print()

    # --------------------------------
    # NAME
    # --------------------------------

    name = get_non_empty_string(
        "ENTER MEMBER NAME - "
    )

    # --------------------------------
    # DESIGNATION
    # --------------------------------

    designation = get_designation()

    # --------------------------------
    # DOB
    # --------------------------------

    dob = get_date(
        "ENTER MEMBER'S DATE OF BIRTH "
        "(YYYY-MM-DD) - ",
        "%Y-%m-%d"
    )

    # --------------------------------
    # USERNAME
    # --------------------------------

    while True:

        username = get_non_empty_string(
            "ENTER USERNAME OF MEMBER - "
        )

        existing = members[
            members["username"]
            .astype(str)
            .str.lower()
            .eq(username.lower())
        ]

        if existing.empty:
            break

        print("USERNAME ALREADY TAKEN.")
        print("CHOOSE A DIFFERENT USERNAME.")

    # --------------------------------
    # USER ID
    # --------------------------------

    while True:

        user_id = get_user_id()

        existing = members[
            members["user_id"]
            .astype(str)
            .eq(str(user_id))
        ]

        if existing.empty:
            break

        print("USER ID ALREADY TAKEN.")
        print("CHOOSE A DIFFERENT USER ID.")

    # --------------------------------
    # GAME
    # --------------------------------

    game_name = get_game_name()

    # --------------------------------
    # DATABASE INSERT
    # --------------------------------

    add_member(
        connection,
        name,
        designation,
        dob,
        username,
        user_id,
        game_name
    )

    # --------------------------------
    # REFRESH LOCAL MEMBER DATA
    # --------------------------------

    return load_members(connection)


def manager_member_database(connection, members):
    """
    Manager's member database menu.
    """

    while True:

        print()
        print("-*" * 20)
        print()

        print(
            "PRESS 1 TO VIEW THE OUTSET MEMBER DATABASE"
        )

        print(
            "PRESS 2 TO ADD A MEMBER TO THE OUTSET FAMILY"
        )

        choice = get_choice(
            "---------> ",
            {"1", "2"}
        )

        # --------------------------------
        # VIEW DATABASE
        # --------------------------------

        if choice == "1":

            print()
            print(members.to_string(index=False))
            print()

        # --------------------------------
        # ADD MEMBER
        # --------------------------------

        elif choice == "2":

            members = add_new_member(
                connection,
                members
            )

            print()
            print(
                members.to_string(index=False)
            )

        cont = get_yes_no(
            "DO YOU WANT TO ACCESS OUTSET "
            "DATABASE AGAIN? (Y/N) "
        )

        if cont == "n":
            break

    return members


def manager_menu(connection, members):
    """
    Main Manager menu.
    """

    print("WELCOME MANAGER")

    while True:

        print()
        print("PRESS 1 TO VIEW/EDIT THE DATA")
        print("PRESS 2 TO ACCESS OUTSET MEMBER DATABASE")

        choice = get_choice(
            "----> ",
            {"1", "2"}
        )

        # --------------------------------
        # GAME DATA
        # --------------------------------

        if choice == "1":

            print()
            print("YOU CHOSE TO VIEW/EDIT DATA")

            manager_game_menu()

        # --------------------------------
        # MEMBER DATABASE
        # --------------------------------

        elif choice == "2":

            print(
                "ACCESSING OUTSET MEMBER DATABASE..."
            )

            members = manager_member_database(
                connection,
                members
            )

        cont = get_yes_no(
            "DO YOU WANT TO CONTINUE? (Y/N) "
        )

        if cont == "n":
            print("EXITING SYSTEM...")
            break

    return members


# ============================================================
# IGL / GAMER FUNCTIONS
# ============================================================

def get_user_game_data(user):
    """
    Determine the game assigned to the logged-in user
    and load its CSV data.
    """

    game_name = str(
        user["game_name"]
    ).strip()

    if game_name not in GAME_FILES:

        raise ValueError(
            f"INVALID GAME ASSIGNED TO USER: {game_name}"
        )

    dataframe = load_game_data(
        game_name,
        GAME_FILES
    )

    return game_name, dataframe


def edit_user_game_data(game_name, dataframe):
    """
    Edit the game assigned to an IGL.
    """

    print(
        f"YOU CHOSE TO EDIT THE DATA OF {game_name}"
    )

    print()

    print(dataframe.to_string(index=False))

    while True:

        date = get_date(
            "ENTER DATE (DD-MM-YYYY) - "
        )

        games_won = get_integer(
            "ENTER GAMES WON - ",
            minimum=0
        )

        games_lost = get_integer(
            "ENTER GAMES LOST - ",
            minimum=0
        )

        rounds_won = get_integer(
            "ENTER ROUNDS WON - ",
            minimum=0
        )

        rounds_lost = get_integer(
            "ENTER ROUNDS LOST - ",
            minimum=0
        )

        dataframe = add_game_record(
            dataframe,
            date,
            games_won,
            games_lost,
            rounds_won,
            rounds_lost
        )

        save_game_data(
            dataframe,
            game_name,
            GAME_FILES
        )

        print("RECORD ADDED SUCCESSFULLY.")

        again = get_yes_no(
            "DO YOU WANT TO EDIT DATA AGAIN? (Y/N) "
        )

        if again == "n":
            break

    return dataframe


def igl_menu(user):
    """
    IGL menu.
    """

    print("WELCOME IGL")

    game_name, dataframe = get_user_game_data(
        user
    )

    print()
    print("-*" * 10)
    print()

    while True:

        choice = get_yes_no(
            "DO YOU WANT TO VIEW OR EDIT DATA? (Y/N) "
        )

        if choice == "n":

            print("THANK YOU FOR VISITING")
            break

        print()
        print("PRESS 1 FOR EDITING THE DATA")
        print("PRESS 2 FOR VIEWING THE DATA")

        action = get_choice(
            "--------> ",
            {"1", "2"}
        )

        if action == "1":

            dataframe = edit_user_game_data(
                game_name,
                dataframe
            )

        elif action == "2":

            print(
                f"YOU CHOSE TO VIEW THE DATA OF "
                f"{game_name}"
            )

            view_data(dataframe)


def gamer_menu(user):
    """
    Gamer menu.
    """

    print("WELCOME GAMER")

    game_name, dataframe = get_user_game_data(
        user
    )

    print(
        f"VIEWING {game_name} DATA"
    )

    view_data(dataframe)


# ============================================================
# MAIN
# ============================================================

def main():

    connection = None

    try:

        # --------------------------------
        # DATABASE
        # --------------------------------

        connection = get_connection(
            DB_CONFIG
        )

        members = load_members(
            connection
        )

        # --------------------------------
        # LOGIN
        # --------------------------------

        user = authenticate_user(
            members
        )

        if user is None:
            return

        # --------------------------------
        # ROLE
        # --------------------------------

        designation = str(
            user["designation"]
        ).strip()

        if designation == "Manager":

            manager_menu(
                connection,
                members
            )

        elif designation == "IGL":

            igl_menu(user)

        elif designation == "Gamer":

            gamer_menu(user)

        else:

            print(
                f"ERROR: UNKNOWN DESIGNATION "
                f"'{designation}'"
            )

    except KeyboardInterrupt:

        print()
        print("PROGRAM TERMINATED BY USER.")

    except Exception as error:

        print()
        print(
            f"APPLICATION ERROR: {error}"
        )

    finally:

        if connection is not None:

            try:
                connection.close()
                print("DATABASE CONNECTION CLOSED.")

            except Exception:
                pass


if __name__ == "__main__":
    main()
