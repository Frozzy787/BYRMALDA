class Grandpa:
    def __init__(self):
        self.age = 70

    def fishing(self):
        print("Дідусь рибалить")


class Dad:
    def __init__(self):
        self.car = "BMW"

    def drive(self):
        print("Тато водить машину")


class Son(Grandpa, Dad):
    def __init__(self):
        Grandpa.__init__(self)
        Dad.__init__(self)

    def play(self):
        print("Син грає")


son = Son()

print("Вік дідуся:", son.age)
print("Машина тата:", son.car)

son.fishing()
son.drive()
son.play()