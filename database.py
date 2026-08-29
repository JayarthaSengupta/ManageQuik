import mysql.connector as sqltor
import pandas as pd


def get_connection(config):
    try:
        connection = sqltor.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
        )

        print("DATABASE CONNECTION SUCCESSFUL")
        return connection

    except sqltor.Error as error:
        raise ConnectionError(f"Could not connect to database: {error}")


def load_members(connection):
    """
    Load all members from the emp table.
    """

    try:
        query = "SELECT * FROM emp"

        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)

        records = cursor.fetchall()
        cursor.close()

        return pd.DataFrame(records)

    except sqltor.Error as error:
        raise RuntimeError(f"Could not load member database: {error}")


def add_member(connection, name, designation, dob, username, user_id, game_name):

    query = """
        INSERT INTO emp
        (name, designation, dob, username, user_id, game_name)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (name, designation, dob, username, user_id, game_name)

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()

        print("MEMBER SUCCESSFULLY ADDED.")

    except sqltor.Error as error:
        connection.rollback()

        raise RuntimeError(f"Could not add member: {error}")
