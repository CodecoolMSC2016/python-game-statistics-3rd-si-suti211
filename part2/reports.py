
# Report functions


def get_most_played(file_name="game_stat.txt"):
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # finding most sold game Index
    maxi = 0
    for i in range(len(salesList)):
        if float(salesList[i][1]) > float(salesList[maxi][i]):
            maxi = i

    # if there is more games with the same sale values,
    # we return the one with the lower index
    if salesList.count(salesList[maxi][1] > 1):
        return salesList[salesList.index(salesList[maxi][1])][0]
    return salesList[maxi][0]
