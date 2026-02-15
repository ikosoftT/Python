class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.Age: int = age

    def grow(self):
        self.height += 1

    def age(self):
        self.Age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{i + 1}cm")
