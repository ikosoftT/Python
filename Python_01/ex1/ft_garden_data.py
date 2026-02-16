class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    data_names: str = ["Rose", "Sunflower", "Cactus"]
    data_heights: int = [25, 80, 15]
    data_ages: int = [30, 45, 120]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        plant: Plant = Plant(data_names[i], data_heights[i], data_ages[i])
        plant.get_info()
