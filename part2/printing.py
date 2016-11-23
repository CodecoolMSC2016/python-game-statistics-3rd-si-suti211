import reports
# Printing functions


def main():
    print(reports.get_most_played())
    print(reports.sum_sold())
    print(reports.get_selling_avg())
    print(reports.count_longest_title())
    print(reports.get_date_avg())
    print(reports.get_game("Half-Life 2"))
    print(reports.count_grouped_by_genre())

if __name__ == "__main__":
    main()
