
# Report functions
# returns the name of the most sold(played) game


def get_most_played(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # finding most sold game Index
    maxi = 0
    for i in range(len(salesList)):
        if float(salesList[i][1]) > float(salesList[maxi][1]):
            maxi = i

    # we scan the sales, and determine how many games have the same
    # sale value

    gamesWithSameSales = 0
    for i in range(len(salesList)):
        if float(salesList[i][1]) == float(salesList[maxi][1]):
            gamesWithSameSales += 1

    # if we have more than 1 game with the same sale values as the
    # most popular we find the one with the lower index and return it

    if gamesWithSameSales > 1:
        for i in range(len(salesList)):
            if salesList[i][1] == salesList[maxi][1]:
                return salesList[i][0]
    else:
        return salesList[maxi][0]


# returns the sum of game sales


def sum_sold(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # getting the sum of game sales
    sumOfSales = 0.0

    for game in range(len(salesList)):
        sumOfSales += float(salesList[game][1])

    return sumOfSales


# gets the avg of sellings


def get_selling_avg(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # getting the sum of game sales
    sumOfSales = 0.0

    # we only add the sales of the current game to the sum,
    # if its not in the checked list, to avoid counting issues
    # caused by multiple occurance of the same game
    checkedList = []
    for game in range(len(salesList)):
        if salesList[game][0] not in checkedList:
            sumOfSales += float(salesList[game][1])
            checkedList.append(salesList[game][0])

    return sumOfSales / len(checkedList)


# getting the longest title, and returning its length


def count_longest_title(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # find the longest title
    maxi = 0
    for game in range(len(salesList)):
        if len(salesList[game][0]) > len(salesList[maxi][0]):
            maxi = game
    return len(salesList[maxi][0])

# gets the avg of the release years


def get_date_avg(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # getting the sum of game releases
    sumOfReleases = 0.0

    for game in range(len(salesList)):
        sumOfReleases += float(salesList[game][2])

    # adding 0.5 to the avg then converting it to int
    # to mimic a rounding method
    return int(sumOfReleases / len(salesList) + 0.5)

# gets all data of a selected game


def get_game(file_name, title):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # finding the first game that matches string given in title
    gameProperties = []
    for game in range(len(salesList)):
        if salesList[game][0] == title:
            gameProperties.append(salesList[game][0])
            gameProperties.append(float(salesList[game][1]))
            gameProperties.append(int(salesList[game][2]))
            gameProperties.append(salesList[game][3])
            gameProperties.append(salesList[game][4])
            return gameProperties
    raise ValueError

# gets games / genre


def count_grouped_by_genre(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    genres = {}

    # if the current games genre is not in the genres dictionary
    # we add it with a 0+1 default value
    for game in range(len(salesList)):
        if salesList[game][3] not in genres:
            genres.update(
                {salesList[game][3]: genres.get(salesList[game][3], 0) + 1})
        # if its in, we just update the key with an incremented value
        else:
            genres.update(
                {salesList[game][3]: genres.get(salesList[game][3]) + 1})

    return genres


def get_date_ordered(file_name="game_stat.txt"):
    # getting file contents into a list
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    salesList = sorted(salesList, key=lambda x: x[2], reverse=True)

    titlesOnlyList = []

    for i in range(len(salesList)):
        titlesOnlyList.append(salesList[i][0])

    return titlesOnlyList
