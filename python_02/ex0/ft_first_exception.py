def check_temperature(temp_str: str) -> int | None:
    try:
        conv = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if 0 <= conv <= 40:
            print(f"Temperature {conv}°C is perfect for plants!\n")
            return conv
        elif conv > 40:
            print(f"Error: {conv}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {conv}°C  is too cold for plants (min 0°C)")
    return None


def test_temperature() -> None:
    data: list[str] = ["25", "abc", "100", "-50"]
    for d in data:
        print(f"Testing temperature: {d}")
        check_temperature(d)
    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
