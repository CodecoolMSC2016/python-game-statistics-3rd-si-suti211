import reports as r
# Export functions


def write_list_tabbed(list, file):
    for i in list:
        file.write("\t" + str(i) + "\n")


def main():
    EXPORT_FILE = "reports.txt"
    FILE_NAME = "game_stat.txt"

    with open(EXPORT_FILE, "w") as file:
        file.write("The top played game is {0:s}.\n".format(
            r.get_most_played()))
        file.write(
            "Total game copies sold: {0:.3f} million.\n".format(r.sum_sold()))
        file.write("The average selling was {0:.3f} million.\n".format(
            r.get_selling_avg()))
        file.write("The longest game title is {0:d} characters long.\n".format(
            r.count_longest_title()))
        file.write("The average of the release dates is {0:d}\n".format(
            r.get_date_avg()))

        game_to_examine = input(
            "Which games' properties would you like to see?: ")

        file.write("Properties of {0:s}:\n".format(game_to_examine))
        write_list_tabbed(r.get_game(FILE_NAME, game_to_examine), file)

        file.write("\nTotal games by genre:\n")
        genres = r.count_grouped_by_genre()

        for k in genres:
            file.write("\t{0:s} : {1:d}\n".format(k, genres.get(k)))
        file.write("\nAvailable games sorted by release date: \n")
        write_list_tabbed(r.get_date_ordered(), file)

if __name__ == "__main__":
    main()
