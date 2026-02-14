class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted:", end='')
            print(f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected", end="\n\n")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted:", end='')
            print(f" age {age} days [REJECTED]")
            print("Security: Negative age rejected", end="\n\n")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    plant = SecurePlant("Rose")
    plant.set_height(-25)
    plant.set_age(30)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm,", end='')
    print(f" {plant.get_age()} days)")
