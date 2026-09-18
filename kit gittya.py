class Cat:
    def __init__(self):
        self.hunger = 50
        self.happy = 50

    def eat(self):
        self.hunger += 40
        print("Сьома поїв")

    def play(self):
        self.happy += 30
        print("Сьома погрався")

    def sleep(self):
        print("Сьома поспав")


cat = Cat()

cat.eat()
cat.play()
cat.sleep()

print("Голод:", cat.hunger)
print("Щастя:", cat.happy)
