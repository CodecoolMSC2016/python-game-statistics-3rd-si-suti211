import reports
# Export functions


def print_list(list, file):
    for i in list:
        file.write("\t {0:s}\n".format(i))


def main():
    EXPORT_FILE = "answers.txt"
    FILE_NAME = "game_stat.txt"
    with open(EXPORT_FILE, "w") as file:
        file.write("There are {0:d} games in the file.\n".format(
            reports.count_games(FILE_NAME)))

        file.write("Is there any game released in 1997?: {0:s}".format("yes.\n" if
                                                                       reports.decide(FILE_NAME, 1997) else "no.\n"))
        file.write("Latest game release was: {0:s}.\n".format(
            reports.get_latest(FILE_NAME)))
        file.write("There are {0:d} RPG games out there.\n".format(
            reports.count_by_genre(FILE_NAME, "RPG")))
        file.write("The serial number of Half-Life 2 is: {0:d}.\n".format(
            reports.get_line_number_by_title(FILE_NAME, "Half-Life 2")))

        file.write("Available game genres:\n")
        genres = reports.get_genres(FILE_NAME)
        print_list(genres, file)

        file.write("\nRelease date of top sold fps: {0:d}.\n".format(
            reports.when_was_top_sold_fps(FILE_NAME)))

        file.write("\nAvailable game titles:\n")
        game_titles = reports.sort_abc(FILE_NAME)
        print_list(game_titles, file)

        print("Exporting finished, check the %s file!" % (EXPORT_FILE))


if __name__ == "__main__":
    main()
