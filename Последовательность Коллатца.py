def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


number = ""
while True:
    try:
        number = int(input("Введите число:\n"))
    except ValueError:
        print("Вы ввели не число!")
    if number:
        break
print(number)
while number != 1:
    number = collatz(number)
    print(number)
