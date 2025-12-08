from time import sleep

def mass():

    def err():
        print("Перезапуск функции...")
        sleep(3)
        mass()
    global result
    n1 = int(input("Напишите исходное число: "))
    e1 = input("Напишите исходную единицу измерения (мг|кг|г|т): ")
    e2 = input("Напишите единицу измерения в которую хотите перевести (мг|кг|г|т): ") # TODO: Добавить еще единиц измерения
    if e1 == "кг":
        if e2 == "г":
            result = n1 * 1000
        elif e2 == "кг":
            result = n1
        elif e2 == "т":
            result = n1 / 1000
        elif e2 == "мг":
            result = n1 * 1000000
        else:
            err()
    elif e1 == "г":
        if e2 == "кг":
            result = n1 / 1000
        elif e2 == "г":
            result = n1
        elif e2 == "т":
            result = n1 / 1000000
        elif e2 == "мг":
            result = n1 * 1000
        else:
            err()
    elif e1 == "т":
        if e2 == "кг":
            result = n1 * 1000
        elif e2 == "г":
            result = n1 * 1000000
        elif e2 == "т":
            result = n1
        elif e2 == "мг":
            result = n1 * 1000000000
        else:
            err()
    elif e1 == "мг":
        if e2 == "кг":
            result = n1 / 1000000
        elif e2 == "г":
            result = n1 / 1000
        elif e2 == "т":
            result = n1 / 1000000000
        elif e2 == "мг":
            result = n1
        else:
            err()
    else:
        err()

    print(f"Результат: {n1} {e1} = {result} {e2}")

print("=" * 27)
print("\tКалькулятор величин\t")
print("=" * 27)
print("")

while True:
    print("""
Советуем прочитать README.md перед использованием программы

Доступные величины:
1) Масса
    """) # TODO: Сделать еще больше величин

    option = input("Выберите одну из представленных величин: ")
    if option == "1":
            mass() # TODO: README
            opt = input("Еще? ")
    if opt == "нет":
        break