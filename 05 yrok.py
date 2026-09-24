import colorama

print("Атрибути та методи бібліотеки colorama:")
print(dir(colorama))

print("Основні елементи:")

print("Fore — задає колір тексту.")
print("init() — налаштовує роботу colorama.")
print("deinit() — вимикає colorama.")
print("reinit() — повторно вмикає colorama.")

colorama.init()

print(colorama.Fore.RED + "Червоний текст")
print(colorama.Fore.GREEN + "Зелений текст")
print(colorama.Fore.BLUE + "Синій текст")`