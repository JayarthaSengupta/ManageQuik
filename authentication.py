def validate_user_id(user_id):
    user_id = str(user_id)
    return (
        user_id.isdigit()
        and len(user_id) == 6
    )


def authenticate_user(members):
    if members.empty:
        print("ERROR: NO USERS FOUND IN DATABASE.")
        return None
    
    while True:
        username = input("ENTER USERNAME - ").strip()
        user_id = input("ENTER USER ID - ").strip()

        # USER ID VALIDATION
        # -------------------------
        if not validate_user_id(user_id):
            print("ERROR 01: INVALID USER ID")
            print("USER ID MUST CONTAIN EXACTLY 6 DIGITS.")
            continue

        # USERNAME SEARCH
        # -------------------------
        matching_users = members[
            members["username"]
            .astype(str)
            .str.lower()
            .eq(username.lower())
        ]

        if matching_users.empty:
            print("ERROR 02: INVALID USERNAME")
            continue

        # USER ID SEARCH
        # -------------------------
        matching_user = matching_users[
            matching_users["user_id"]
            .astype(str)
            .eq(user_id)
        ]

        if matching_user.empty:
            print("ERROR 01: INVALID USER ID")
            continue

        # SUCCESS
        # -------------------------
        user = matching_user.iloc[0].to_dict()
        print()
        print("LOGIN SUCCESSFUL")
        print()

        return user