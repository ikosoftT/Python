class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.Age = age

    def grow(self):
        self.height += 1

    def age(self):
        self.Age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Cactus", 25, 60)
    print("=== Day 1 ===")
    plant1.get_info()
    plant2.get_info()
    for i in range(6):
        plant1.grow()
        plant2.grow()
        plant1.age()
        plant2.age()
    print("=== Day 7 ===")
    plant1.get_info()
    plant2.get_info()
    print(f"Growth this Week: +{plant1.height + plant2.height}cm")
