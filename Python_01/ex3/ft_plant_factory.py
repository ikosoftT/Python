class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    data_names: str = ["Rose", "Sunflower", "Cactus", "Fern", "Oak"]
    data_heights: int = [25, 200, 5, 80, 15]
    data_ages: int = [30, 45, 120, 365, 90]
    print("=== Plant Factory Output ===")
    for i in range(5):
        plant = Plant(data_names[i], data_heights[i], data_ages[i])
        plant.get_info()
    print("", end="\n\n")
    print(f"Total plants craeted: {i + 1}")
