
# Report functions


def get_most_played(file_name="game_stat.txt"):
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
