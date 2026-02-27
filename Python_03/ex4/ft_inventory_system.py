import sys


def parsing_data() -> dict:
    if len(sys.argv) <= 1:
        raise ValueError("No Arguments Provided!")
    colon: int = -1
    data = {}
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        j = 0
        while j < len(arg):
            if arg[j] == ":":
                colon = j
                break
            j += 1
        if colon == -1:
            raise ValueError("Enter Valid args key:value")
        key = arg[:colon]
        value = arg[colon + 1:]
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Converting '{value}' to int()")
        data.update({key: value})
        i += 1
    return data


def current_inventory(data: dict, total: int) -> None:
    percent: int = 0
    for key in data.keys():
        if total == 0:
            percent = 0
        else:
            percent = (data.get(key) / total) * 100
        print(f"{key}: {data.get(key)} units ({percent:.1f}%)")


def item_categories(data: dict) -> dict:
    category = {
        "Moderator": {},
        "Scarce": {}
    }
    for key, value in data.items():
        if value >= 5:
            category['Moderator'].update({key: value})
        else:
            category['Scarce'].update({key: value})
    return category


def invetory_static(data: dict) -> dict:
    Most: str = None
    Least: str = None
    for key, value in data.items():
        if Most is None or value > data[Most]:
            Most = key
        if Least is None or value < data[Least]:
            Least = key
    print(f"Most abundant: {Most} ({data[Most]} units)")
    print(f"Least abundant: {Least} ({data[Least]} units)")


def manage_suggestions(data: dict) -> None:
    restock: list[str] = []
    for key, value in data.items():
        if value <= 1:
            restock += [key]
    print("Restock needed: ", end='')
    i = 0
    while i < len(restock):
        if i < len(restock) - 1:
            print(restock[i], end=',')
        else:
            print(restock[i])
        i += 1
    if not restock:
        print("Inventory levels are healthy.")


def main() -> None:
    data: dict = parsing_data()
    total: int = 0

    print("=== Inventory System Analysis ===")

    for val in data.values():
        total += val

    print(f"Total items in inventory: {total}")

    print(f"Unique item types: {len(data)}")

    print("\n=== Current Inventory ===")
    current_inventory(data, total)
    print("\n=== Inventory Statistics ===")
    invetory_static(data)
    print("\n=== Item Categories ===")
    category = item_categories(data)
    print(f"Moderate: {category['Moderator']}")
    print(f"Scarce: {category['Scarce']}")
    print("\n=== Management Suggestions ===")
    manage_suggestions(data)
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary Keys: ", end='')
    print(*data.keys(), sep=", ")
    print("Dictionary Values: ", end='')
    print(*data.values(), sep=", ")
    stat = False
    if data['sword']:
        stat = True
    else:
        stat = False
    print(f"Sample lookup - 'sword' in inventory: {stat}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
