def calculator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except:
            print("Помилка у виразі")
    return wrapper


@calculator
def calculate(expression):
    return eval(expression)


print(calculate("5 + 3"))
print(calculate("10 / 2"))
print(calculate("5 / 0"))
