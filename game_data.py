from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["Date", "Games Won", "Games Lost", "Rounds Won", "Rounds Lost"]


def load_game_data(game_name, game_files):
    # Load game data from the appropriate CSV file

    if game_name not in game_files:
        raise ValueError(f"Unsupported game: {game_name}")

    filepath = Path(game_files[game_name])

    if not filepath.exists():
        raise FileNotFoundError(f"Game data file not found: {filepath}")

    try:
        dataframe = pd.read_csv(filepath)

    except Exception as error:
        raise RuntimeError(f"Could not read {filepath}: {error}")

    # CHECK CSV STRUCTURE
    # --------------------------------
    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"{filepath} is missing columns: {', '.join(missing_columns)}")

    # REMOVE EMPTY RECORDS
    # --------------------------------
    dataframe = dataframe.dropna().reset_index(drop=True)

    return dataframe


def add_game_record(dataframe, date, games_won, games_lost, rounds_won, rounds_lost):
    # Add a new game record to the dataframe.

    new_record = pd.DataFrame(
        [
            {
                "Date": date,
                "Games Won": games_won,
                "Games Lost": games_lost,
                "Rounds Won": rounds_won,
                "Rounds Lost": rounds_lost,
            }
        ]
    )

    return pd.concat([dataframe, new_record], ignore_index=True)


def save_game_data(dataframe, game_name, game_files):
    # Persist modified game data back to its CSV file.

    if game_name not in game_files:
        raise ValueError(f"Unsupported game: {game_name}")

    filepath = Path(game_files[game_name])

    try:
        dataframe.to_csv(filepath, index=False)

    except Exception as error:
        raise RuntimeError(f"Could not save game data: {error}")

    print(f"GAME DATA SUCCESSFULLY SAVED TO {filepath}")