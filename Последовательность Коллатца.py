def collatz(number):
    if not number % 2:
        return number // 2
    else:
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
