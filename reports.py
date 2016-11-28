# Report functions
# constants for indexing the 2D list in a more readable way
TITLE_INDEX = 0
SALES_INDEX = 1
RELEASE_INDEX = 2
GENRE_INDEX = 3
PUBLISHER_INDEX = 4


def count_games(file_name):
    """
    Gets how many lines a file has.
    Arguments:
    file_name - string, name of the file which we open
    returns an int.
    """
    gameCount = 0
    with open(file_name, "r") as file:
        for lines in file:
            gameCount += 1
    return gameCount


def decide(file_name, year):
    """Returns true if there was any game release in year given in parameters.
    returns false otherwise.

    Arguments:
        file_name - existing file name (string)
        year - checkable year(int)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # check if we have any entry matching parameter "year"
    # the third element of the sublist will be always the release year
    for game in salesList:
        if int(game[RELEASE_INDEX]) == year:
            return True
    return False


def get_latest(file_name):
    """Gets the title of the game with the latest release
    returns a string.
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    # finding maximum in release dates
    maxi = 0
    for game in range(len(salesList)):
        if int(salesList[game][RELEASE_INDEX]) > int(salesList[maxi][RELEASE_INDEX]):
            maxi = game

    gamesWithSameRelease = 0
    for game in range(len(salesList)):
        if float(salesList[game][RELEASE_INDEX]) == float(salesList[maxi][RELEASE_INDEX]):
            gamesWithSameRelease += 1

    # if we have more than 1 game with the same release date
    if gamesWithSameRelease > 1:
        for game in range(len(salesList)):
            if salesList[game][RELEASE_INDEX] == salesList[maxi][RELEASE_INDEX]:
                return salesList[game][TITLE_INDEX]
    else:
        return salesList[maxi][TITLE_INDEX]


def count_by_genre(file_name, genre):
    """Returns how much games a selected genre has.

    Arguments:
    file_name - file for reading (str)
    genre - game genre (str)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    genreCount = 0

    # the fourth element of the sublist is always the genre
    for game in range(len(salesList)):
        if salesList[game][GENRE_INDEX] == genre:
            genreCount += 1

    return genreCount


def get_line_number_by_title(file_name, title):
    """Gets the first line number where the given title matches with the game_stat list
    if no match found, raises a ValueError

    Arguments:
    file_name - file name for reading (str)
    title - the game title we searching for (str)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    serialNumber = 0
    for game in range(len(salesList)):
        if salesList[game][TITLE_INDEX] == title:
            serialNumber = game + 1
            break
    if serialNumber == 0:
        raise ValueError

    return serialNumber


def get_genres(file_name):
    """Get all game genres, and returns it as a list (no duplicates).

    Arguments:
    file_name - the name of the file we read from (str)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))
    genreList = []

    # getting all genres into an empty list
    for game in range(len(salesList)):
        genreList.append(salesList[game][GENRE_INDEX])

    # this eliminates duplicate elements
    genreListFiltered = [ii for n, ii in enumerate(
        genreList) if ii not in genreList[:n]]

    # sorting alphabetically
    genreListFiltered = sorted(genreListFiltered, key=lambda x: x.lower())
    return genreListFiltered


def when_was_top_sold_fps(file_name):
    """Finds the top selling fps, return its release year as (int)

    Arguments:
    file_name - the name of the file we read from (str)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t"))

    fpsList = []

    # getting all the fps games into a separate list
    for game in range(len(salesList)):
        if salesList[game][GENRE_INDEX] == "First-person shooter":
            helperList = [salesList[game][TITLE_INDEX], salesList[
                game][SALES_INDEX], salesList[game][RELEASE_INDEX]]
            fpsList.append(helperList)

    # if we ave any fps game find the one with the greatest sales
    # and returning its release
    maxi = 0
    if len(fpsList) == 0:
        raise ValueError
    else:
        for game in range(len(fpsList)):
            if float(fpsList[game][SALES_INDEX]) > float(fpsList[maxi][SALES_INDEX]):
                maxi = game
        return int(fpsList[maxi][RELEASE_INDEX])


def sort_abc(file_name):
    """Sorting file contents

    Arguments:
    file_name - the name of the file we read from (str)
    """
    salesList = []
    with open(file_name, "r") as file:
        for lines in file:
            salesList.append(lines.strip("\n").split("\t")[0])

    salesList.sort()
    return salesList
