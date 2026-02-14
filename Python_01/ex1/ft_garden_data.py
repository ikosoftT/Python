class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant_names = ["Rose", "Sunflower", "Cactus"]
    plant_heights = [25, 80, 15]
    plant_age = [30, 45, 120]

    for i in range(3):
        plant = Plant(plant_names[i], plant_heights[i], plant_age[i])
        plant.get_info()
