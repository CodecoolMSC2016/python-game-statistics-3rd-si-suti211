import reports
# Printing functions

FILE_NAME = "game_stat.txt"
print(reports.get_genres(FILE_NAME))
print(reports.sort_abc(FILE_NAME))
print(reports.count_games(FILE_NAME))
print(reports.decide(FILE_NAME, 1997))
print(reports.count_by_genre(FILE_NAME, "RPG"))
print(reports.get_latest(FILE_NAME))
print(reports.get_line_number_by_title(FILE_NAME, "World of Warcraft"))
