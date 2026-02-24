import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y1 + y2) ** 2 + (z1 + z2) ** 2)


def parse_coordinates(coord_str: str) -> tuple:
    try:
        parts = coord_str.split(",")
        if len(parts) != 3:
            raise ValueError("Coordinate must be 3 values")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error Parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
    return None


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    position: tuple = (10, 20, 5)
    print(f"Position created: {position}")

    origin: tuple = (0, 0, 0)
    distance = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")

    coord_inp = "3,4,0"

    print(f"Parsing coordinates: \"{coord_inp}\"")
    parsed_coord = parse_coordinates(coord_inp)

    print(f"Parsed position: {parsed_coord}")
    dis = calculate_distance(origin, parsed_coord)

    print(f"Distance between {origin} and {parsed_coord}: {dis:.1f}\n")
    invalid_cord: str = "abc,def,ghi"

    print(f"Parsing invalid coordinates: \"{invalid_cord}\"")
    try:
        parse_coordinates(invalid_cord)
    except ValueError as e:
        print(e)
    if parsed_coord:
        print("Unpacking demonstration:")
        x, y, z = parsed_coord
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
