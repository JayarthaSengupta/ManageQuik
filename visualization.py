import matplotlib.pyplot as plt


def view_data(dataframe):
    # Display game data as a table or graph.

    while True:

        print()
        print("-*" * 15)
        print()

        print(
            "Would you like to view your data "
            "in GRAPH or TABLE format?"
        )

        print("PRESS 1 FOR TABLE FORMAT")
        print("PRESS 2 FOR GRAPH FORMAT")

        print()

        try:
            view_input = int(input("-----> ").strip())

        except ValueError:
            print("ERROR 03: INVALID INPUT")
            continue

        print()
        print("-*" * 15)
        print()

        # TABLE
        # -------------------------
        if view_input == 1:

            print("YOU CHOSE TABLE FORMAT")
            print("-*" * 10)

            print(dataframe.to_string(index=False))

            print("-*" * 10)

            cont = input(
                "DO YOU WANT TO CONTINUE? (Y/N) "
            ).strip().lower()

            if cont == "n":
                print("EXITING VIEW MENU...")
                break

# -------------------------------------------------------------------------

        # GRAPH
        # -------------------------
        elif view_input == 2:

            print("YOU CHOSE GRAPH FORMAT")
            print("-*" * 10)

            rounds_won = dataframe["Rounds Won"]
            rounds_lost = dataframe["Rounds Lost"]
            dates = dataframe["Date"]

            plt.figure(figsize=(10, 6))

            plt.plot(
                dates,
                rounds_won,
                marker="o",
                linestyle="solid",
                label="Rounds Won"
            )

            plt.plot(
                dates,
                rounds_lost,
                marker="o",
                linestyle="solid",
                label="Rounds Lost"
            )

            plt.xlabel("Date")
            plt.ylabel("No. of Rounds")

            plt.title("Rounds Won & Lost")

            plt.grid(True)

            plt.legend(
                loc="upper right"
            )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            plt.show()

            cont = input(
                "DO YOU WANT TO CONTINUE? (Y/N) "
            ).strip().lower()

            if cont == "n":
                print("EXITING VIEW MENU...")
                break

        else:
            print("ERROR 03: INVALID INPUT")