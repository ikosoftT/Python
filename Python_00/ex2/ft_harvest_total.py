def ft_harvest_total() -> None:
    sum = 0
    for i in range(3):
        day: int = int(input(f"Day {i+1} harvest: "))
        sum += day
        i += 1
    print(f"Total harvest: {sum}")
ft_harvest_total()