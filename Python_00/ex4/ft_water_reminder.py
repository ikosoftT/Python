def ft_water_reminder():
    max_days: int = 2
    current_day: int = int(input("Days Since last watering: "))
    if current_day > max_days:
        print("Water the plants!")
    else:
        print("Plants are fine")
