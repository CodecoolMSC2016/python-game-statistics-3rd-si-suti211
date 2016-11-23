import reports
# Export functions


def print_list(list, file):
    for i in list:
        file.write("\t {0:s}\n".format(i))


def main():
    EXPORT_FILE = "exports.txt"
    FILE_NAME = "game_stat.txt"

    release_in_year = int(input("Please enter a year to check: "))
    game_count_by_genre = input("Which genre would you like to summarize?: ")
    line_number_of = input(
        "Which games' serial number would you like to get?: ")

    with open(EXPORT_FILE, "w") as file:
        file.write("There are {0:d} games in the file.\n".format(
            reports.count_games(FILE_NAME)))

        file.write("Is there any game released in {0:d}?: {1:s}".format(release_in_year, "yes.\n" if
                                                                        reports.decide(FILE_NAME, 1997) else "no.\n"))
        file.write("Latest game release was: {0:s}.\n".format(
            reports.get_latest(FILE_NAME)))
        file.write("There are {0:d} {1:s} games out there.\n".format(
            reports.count_by_genre(FILE_NAME, game_count_by_genre), game_count_by_genre))
        file.write("The serial number of {0:s} is: {1:d}.\n".format(line_number_of,
                                                                    reports.get_line_number_by_title(FILE_NAME, line_number_of)))

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
