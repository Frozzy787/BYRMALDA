class Grandpa:
    def __init__(self):
        self.name = "Олег"
        self.age = 70
        self.height = 170


class Dad:
    def __init__(self):
        self.name = "Андрій"
        self.age = 40
        self.height = 177


class Son:
    def __init__(self):
        self.name = "Сьома"
        self.age = 14
        self.height = 165


grandpa = Grandpa()
dad = Dad()
son = Son()

print("Дідусь:", grandpa.name, grandpa.age, "років,", grandpa.height, "см")
print("Тато:", dad.name, dad.age, "років,", dad.height, "см")
print("Син:", son.name, son.age, "років,", son.height, "см")