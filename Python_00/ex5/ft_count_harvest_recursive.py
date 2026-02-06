def helper(day, days) -> None:
    if day > days:
        print("Harvest time!")
    else:
        print("Day", day)
        helper(day + 1, days)


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    helper(1, days)
