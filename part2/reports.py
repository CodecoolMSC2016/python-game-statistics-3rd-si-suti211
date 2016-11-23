
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

    for game in range(len(salesList)):
        sumOfSales += float(salesList[game][1])

    return sumOfSales / len(salesList)


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
