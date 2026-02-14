class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.Age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.Age} days)")


if __name__ == "__main__":
    plant_names = ["Rose", "Sunflower", "Cactus", "Fern", "Oak"]
    plant_heights = [25, 200, 5, 80, 35]
    plant_age = [30, 365, 90, 45, 120]
    print("=== Plant Factory Output ===")
    for i in range(5):
        plant = Plant(plant_names[i], plant_heights[i], plant_age[i])
        plant.get_info()
    print("")
    print(f"Total plants created:  {i+1}")
