import reports
# Export functions


def main():
    FILE_NAME = "game_stat.txt"
    with open("answers.txt", "w") as file:
        file.write("There are {0:d} games in the file.".format(
            reports.count_games(FILE_NAME)))

        file.write("Is there any game released in 1997?: {0:s}.".format(
            reports.decide(FILE_NAME, 1997)))

if __name__ == "__main__":
    main()
