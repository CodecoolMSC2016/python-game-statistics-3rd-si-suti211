
# Report functions


def count_games(file_name):
    gameCount = 0
    with open(file_name, "r") as file:
        for lines in file:
            gameCount += 1
    return gameCount


def decide(file_name, year):
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    for i in range(len(salesList)):
        if int(salesList[i][2]) == year:
            return True
    return False


def get_latest(file_name):
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # finding maximum in release dates
    maxi = 0
    for i in range(len(salesList)):
        if int(salesList[i][2]) > int(salesList[maxi][2]):
            maxi = i
    # if we have more than 1 game with the same release year,
    # we return the first element(name)of the element with the lowest index
    if salesList.count(salesList[maxi][2]) > 1:
        return str(salesList[salesList.index(salesList[maxi][2])][0])
    else:
        return str(salesList[maxi][0])


def count_by_genre(file_name, genre):
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    genreCount = 0

    for i in range(len(salesList)):
        if salesList[i][3] == genre:
            genreCount += 1

    return genreCount


def get_line_number_by_title(file_name, title):
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    serialNumber = 0
    for i in range(len(salesList)):
        if salesList[i][0] == title:
            serialNumber = i + 1
            break
    if serialNumber == 0:
        raise ValueError

    return serialNumber

print(count_games("game_stat.txt"))
print(decide("game_stat.txt", 2002))
print(get_latest("game_stat.txt"))
print(count_by_genre("game_stat.txt", "RPG"))
print(get_line_number_by_title("game_stat.txt", "Minecraft"))
