class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!", end="\n\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade", end="\n\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest = harvest_season
        self.value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===", end="\n\n")
    f1 = Flower("Rose", 25, 30, "red color")
    f2 = Flower("Pito", 13, 90, "green color")
    print(f"{f1.name} (Flower): {f1.height}cm, {f1.age} days, {f1.color}")
    f1.bloom()
    print(f"{f2.name} (Flower): {f2.height}cm, {f2.age} days, {f2.color}")
    f2.bloom()
    t1 = Tree("Oak", 500, 1825, "50cm diameter")
    t2 = Tree("Caliptus", 1400, 2825, "150cm diameter")
    print(f"{t1.name} (Tree): {t1.height}cm, {t1.age} days, {t1.trunk}")
    t1.produce_shade()
    print(f"{t2.name} (Tree): {t2.height}cm, {t2.age} days, {t2.trunk}")
    t2.produce_shade()
    m1 = Vegetable("Tomato", 80, 90, "summer harvest", "C")
    m2 = Vegetable("Carot", 50, 95, "Winter harvest", "B")
    print(f"{m1.name} (Vegetable): {m1.height}cm, {m1.age} days, {m1.harvest}")
    print(f"{m1.name} is rich in vitamin {m1.value}", end="\n\n")
    print(f"{m2.name} (Vegetable): {m2.height}cm, {m2.age} days, {m2.harvest}")
    print(f"{m2.name} is rich in vitamin {m2.value}")
